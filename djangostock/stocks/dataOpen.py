import xmltodict
import requests
import json


class KoreaDataAPI:
    KEY = "mjvnG3Ts6jSut9APJky5na2e%2BP3cTvgp%2F7GXhwygXya3qLn3vlCU9o%2FEEKMGhB60BKMzLIdwfkMMtlBcNxtgxg%3D%3D"

    def __init__(self) -> None:
        pass

    def get_lastest_stock_info(self, stock_name):
        """stock_name을 주면 최근 개장일의 주식 시세를 얻을 수 있음

        Args:
            stock_name (_type_): 종목 이름
        
        Return:
            최근 개장일의 주식 시세를 얻을 수 있음

            {'basDt', 'srtnCd': '코드', 'itmsNm': '이름', 'mrktCtg': 'KOSPI', 'mrktTotAmt': '시가총액'}
        """
        url = "https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey=" \
                + KoreaDataAPI.KEY + "&numOfRows=1&pageNo=1&itmsNm=" + str(stock_name)
        res = requests.get(url, verify=False)
        res = xmltodict.parse(res.content)

        stock_info = res['response']['body']['items']['item']
        print("찾아온 주식 정보", res['response']['body']['items']['item'])

        return stock_info


if __name__ == "__main__":
    k = KoreaDataAPI()
    print(k.get_lastest_stock_info("성신양회"))
