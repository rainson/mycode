import scrapy
from scrapy import Request
import re
from ..items import NjHouseItem

class LJSpider(scrapy.Spider):
    name = "ershoufang"
    allowed_domains = ["nj.lianjia.com/ershoufang/"]
    start_urls = ["https://nj.lianjia.com/ershoufang/pg{}/".format(i) for i in range(1,2)]
    def parse(self, response):
        clears = response.css(".sellListContent li")
        print(response, len(clears) )
        for cc in clears:
            # item = NjHouseItem()
            house = cc.css(".houseinfo a::text").extract_first()
            print(cc.css(".houseinfo a::text").extract_first())
            houseinfo = cc.css(".houseinfo::text").extract_first()
            info_list = [info for info in re.split("\|", houseinfo) if len(info)>1]
            house_room = info_list[0].strip()
            house_area = "".join(re.findall(r"[\d+\.]",info_list[1]))
            totalprice = cc.css(".totalprice span::text").extract_first()
            unitprice = re.findall('\d+', cc.css(".unitprice span::text").extract_first())[0]

            # item["house"] = house
            # item["house_area"] = float(house_area)
            # item["unit_price"] = float(unitprice)
            # item["total_price"] = float(totalprice)
            # item["house_room"] = house_room
            print(house)
            # yield item



        # page_info = response.css("div[class='page-box fr']").css("div::attr(page-data)").extract_first()
        # urlist = re.findall("\d+", page_info)
        # next_page = "pg{}/".format(int(urlist[1])+1)
        # url = self.start_urls[0]+next_page
        # print(url)
        # yield Request(url=url, callback=self.parse )




