

def hote_search_url(region_id,near_by_region_id):
    url = 'https://www.opentable.com/s/?'

    if int(near_by_region_id) == 0:
        return url +'regionids='+str(region_id)
    else:
        return url +'regionids='+str(region_id)+'&neighborhoodids='+str(near_by_region_id)


def get_hotel_url(data):
    url='https://www.opentable.com'
    return url+data