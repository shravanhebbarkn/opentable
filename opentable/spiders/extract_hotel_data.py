import datetime
import json


def hotel_schema(name,restaurant_types,hotel_url,latitude,longitude,description,cost_range,menu_last_updated,cuisines
                 ,contact_nos,restaurant_images):
    info = {
        "name":name,
        "restaurant_types":restaurant_types,
        "restaurant_link":hotel_url,
        "latitude":latitude,
        "longitude":longitude,
        "description":description,
        "cost_range":cost_range,
        "menu_last_updated":menu_last_updated,
        "cuisines":cuisines.split(','),
        "contact_nos":contact_nos,
        "restaurant_images":restaurant_images
    }
    return info


def extract_hotel_info(data):
    json_data = json.loads(data.xpath("//script[@class='schema-json']/text()").extract_first())
    name=data.xpath("//title/text()").extract_first() if data.xpath("//title/text()").extract_first() else False
    restaurant_types=json_data['@type'] if json_data['@type'] else False
    hotel_url=data.url if data.url else False
    latitude=json_data['geo']['latitude'] if json_data['geo']['latitude'] else False
    longitude = json_data['geo']['longitude'] if json_data['geo']['longitude'] else False
    description=json_data['description'] if json_data['description'] else False
    cost_range=json_data['priceRange'] if json_data['priceRange'] else False
    menu_last_updated=data.xpath("//div[@class='menu-footer__VussEBoV']/dev/text()").extract_first().split(':')[2] if data.xpath("//div[@class='menu_last_updated']/dev").extract_first() else False
    if menu_last_updated:
     menu_last_updated = datetime.datetime.strptime(menu_last_updated, '%b %d %Y')
    cuisines=data.xpath("//div[@class='e7ff71b6 b2f6d1a4']/text()").extract()[1] if data.xpath("//div[@class='e7ff71b6 b2f6d1a4']/text()").extract()[1] else False
    try:
        contact_nos=data.xpath("//div[@class='e7ff71b6 b2f6d1a4']/text()").extract()[5] if data.xpath("//div[@class='e7ff71b6 b2f6d1a4']/text()").extract()[5] else False
    except:
        contact_nos=False
    restaurant_images=data.xpath("//div[@ class='photo__10vsfGte']/img").extract() if data.xpath("//div[@ class='photo__10vsfGte']/img").extract() else False

    hotel_data=hotel_schema(name=name,restaurant_types=restaurant_types,hotel_url=hotel_url,latitude=latitude,
                            longitude=longitude,description=description,cost_range=cost_range,menu_last_updated=menu_last_updated,cuisines=cuisines,contact_nos=contact_nos,restaurant_images=restaurant_images)
    return hotel_data