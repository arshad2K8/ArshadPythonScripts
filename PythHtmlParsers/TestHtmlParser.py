__author__ = 'arshad'
import requests
from BeautifulSoup import BeautifulSoup

HOF_URL = 'http://www.houseoffraser.co.uk'
urlBenettonHof = 'http://www.houseoffraser.co.uk/Men/BRAND_BENETTON_02,default,sc.html'
urlMensKnitWearHof = 'http://www.houseoffraser.co.uk/knitwear+for+men/201,default,sc.html?cm_sp=NewOffers-_-Offer1Mens-_-Link1'
urlMensOffers = 'http://www.houseoffraser.co.uk/mens-offers/mensoffers,default,pg.html'
urlWomensOffers = 'http://www.houseoffraser.co.uk/womens-offers/womensoffers,default,pg.html?cm_sp=CurrentOffers-_-Womens-_-Link1'

'''
resp = requests.get(urlMensOffers)
html_resp = resp.text
parsed_html = BeautifulSoup(html_resp)

#productSearchRefinementsAjaxContainer > div.bounding-box > div:nth-child(3) > div:nth-child(2)

productSearchRefinementTag = parsed_html.find('div', attrs={'id':'productSearchRefinementsAjaxContainer'})
#print productSearchRefinementTag

offerBoxes = productSearchRefinementTag.findAll('div', attrs={'class':'bounding-box', 'class':'offer-box'})
print 'Offer Boxes length ', len(offerBoxes)
#1.
#newOffersTags = productSearchRefinementTag.findAll('div', attrs={'class':'bounding-box', 'class':'offer-box', 'class':'new-offer'})
newOffersTags = offerBoxes[0].findAll('div', attrs={'class':'new-offer'})
# 2.
dontMissOfferTags = offerBoxes[1].findAll('div', attrs={'class':'section-block'})
#print 'dontMissOfferTags  offers', len(dontMissOfferTags)
#3
weLoveOfferTags = offerBoxes[2].findAll('div', attrs={'class':'section-block'})
#print 'weLoveOfferTags  offers', len(weLoveOfferTags)
#print HOF_URL+newOffersTags[0].find('a')['href']
newOffersHrefs = []

for offer in newOffersTags + dontMissOfferTags + weLoveOfferTags:
    newOffersHrefs.append(HOF_URL+ offer.find('a')['href'])
print 'Length new offers hrefs', len(newOffersHrefs)
print newOffersHrefs

#ListOfferBoxes = productSearchRefinementTag.findAll('div', attrs={'class':'offer-box'})
#print len(ListOfferBoxes)

mainColumndivTag = parsed_html.body.find('div', attrs={'class':'mainColumn'})
#print 'mainColumndivTag', mainColumndivTag

ProdListTags = mainColumndivTag.find('ol', attrs={'class':'product-listing clearfix'}).findAll('li', attrs={'class':'product-list-element'})
print 'Number of product-listing clearfix elements founds ', len(ProdListTags)
prodListingPricesTags = []

ListtupNowWas = []
for prodList in ProdListTags:
    prodListPricestag = prodList.find('div', attrs={'class':'product-listing-prices'})
    prodWasNowTag = prodListPricestag.find('span', attrs={'class':'productPricing wasNow clearfix'})
    if not prodWasNowTag:
        continue
    prodListingPricesTags.append(prodListPricestag)
    prodDesc = prodList.find('div', attrs={'class':'product-description'}).find('span').text
    NowPrice = float(prodWasNowTag.find('span', attrs={'class':'price-now'}).text.strip('Now').strip()[1:])
    WasPrice = float(prodWasNowTag.find('span', attrs={'class':'price-was'}).text.strip('Was').strip()[1:])
    ListtupNowWas.append((prodDesc, NowPrice, WasPrice))
print 'Length is ', len(ListtupNowWas), ListtupNowWas
'''

def getDiscountPercentage(NowPrice, WasPrice):
    discount = (1 - (NowPrice/WasPrice))*100
    return discount

def getNowWasTupGivenUrl(offerUrl):
    print '... Parsing url ', offerUrl
    resp = requests.get(offerUrl)
    html_resp = resp.text
    parsed_html = BeautifulSoup(html_resp)
    #mainColumndivTag = parsed_html.body.find('div', attrs={'class':'mainColumn'})
    failedUrls =[]
    try:
        ProdListTags = parsed_html.find('ol', attrs={'class':'product-listing clearfix'}).findAll('li', attrs={'class':'product-list-element'})
    except AttributeError:
        failedUrls.append(offerUrl)
        print 'Cant parse url', offerUrl
        return []

    ListtupNowWas = []
    for prodList in ProdListTags:
        prodListPricestag = prodList.find('div', attrs={'class':'product-listing-prices'})
        prodWasNowTag = prodListPricestag.find('span', attrs={'class':'productPricing wasNow clearfix'})
        if not prodWasNowTag:
            continue
        prodDesc = prodList.find('div', attrs={'class':'product-description'}).find('span').text
        NowPrice = float(prodWasNowTag.find('span', attrs={'class':'price-now'}).text.strip('Now').strip()[1:])
        WasPrice = float(prodWasNowTag.find('span', attrs={'class':'price-was'}).text.strip('Was').strip()[1:])
        ListtupNowWas.append((prodDesc, NowPrice, WasPrice, getDiscountPercentage(NowPrice, WasPrice)))
    print '... Found items ', len(ListtupNowWas)
    return ListtupNowWas

def getAllOfferUrls(urlMensOffers = 'http://www.houseoffraser.co.uk/mens-offers/mensoffers,default,pg.html'):
    resp = requests.get(urlMensOffers)
    html_resp = resp.text
    parsed_html = BeautifulSoup(html_resp)
    productSearchRefinementTag = parsed_html.find('div', attrs={'id':'productSearchRefinementsAjaxContainer'})
    offerBoxes = productSearchRefinementTag.findAll('div', attrs={'class':'bounding-box', 'class':'offer-box'})

    newOffersTags = offerBoxes[0].findAll('div', attrs={'class':'new-offer'})
    dontMissOfferTags = offerBoxes[1].findAll('div', attrs={'class':'section-block'})
    weLoveOfferTags = offerBoxes[2].findAll('div', attrs={'class':'section-block'})
    newOffersHrefs = []

    for offer in newOffersTags + dontMissOfferTags + weLoveOfferTags:
        newOffersHrefs.append(HOF_URL+ offer.find('a')['href'].encode('utf-8'))

    return newOffersHrefs

if __name__ == "__main__":
    print 'Inside main'

    AllUrls = getAllOfferUrls(urlWomensOffers)
    print 'Length all offers', len(AllUrls)

    AllNowWasTups = []
    for offUrl in AllUrls:
        AllNowWasTups += getNowWasTupGivenUrl(offUrl)
    print 'AllNowWasTups all offers', (AllNowWasTups)
    print 'Found items ', len(AllNowWasTups)