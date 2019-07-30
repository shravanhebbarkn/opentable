# -*- coding: utf-8 -*-
import scrapy
import csv
import sys
from opentable.spiders.extract_hotel_data import extract_hotel_info
from opentable.spiders.url_gen import hote_search_url,get_hotel_url


class OpenTableHotelsSpider(scrapy.Spider):
    name = 'open_table_hotels'

    def start_requests(self):
            url=hote_search_url(region_id=sys.argv[3].split('=')[1],near_by_region_id=sys.argv[5].split('=')[1])
            yield scrapy.FormRequest(url=url,method='GET', callback=self.parse)

    def parse(self, response):
        hotels = response.xpath("//a[@class='rest-row-name rest-name ']/@href").extract()

        for hotel in hotels:
            hotel_url=get_hotel_url(hotel)
            yield scrapy.FormRequest(url=hotel_url,method='GET',callback=self.hotel_info)

    def hotel_info(self,response):
        if response:
            hotel_data=extract_hotel_info(response)
            hotel_csv= open('/home/shravan/Documents/opentable/opentable/hotel_info.csv', 'a')
            csvwriter = csv.writer(hotel_csv)
            csvwriter.writerow(hotel_data.items())
            hotel_csv.close()
