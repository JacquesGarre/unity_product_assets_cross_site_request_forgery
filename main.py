import requests
import bs4 as BeautifulSoup

COOKIE_TOKEN = "" # <= Your csrf token, get it in your cookie named _csrf

url = "https://assetstore.unity.com/packages/3d/environments/fantasy/polygon-fantasy-kingdom-164532" # URL from unity

headers = {
    'authority': "assetstore.unity.com",
    'cache-control': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    'sec-fetch-dest': "document",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    'cookie': "_csrf=" + COOKIE_TOKEN,
    }

response = requests.request("GET", url, headers=headers).text

str_to_find = '"cookies":{"_csrf":"'

csrf_token_index_start = response.find(str_to_find) + len(str_to_find)
csrf_token = str(response[csrf_token_index_start:csrf_token_index_start+32])

url = "https://assetstore.unity.com/api/graphql/batch"

payload = "[{\"query\":\"query CurrentUser {\\n  user(id: $id) {\\n    id\\n    name\\n    email\\n    myAssets\\n    keyImage {\\n      icon24\\n      large\\n      __typename\\n    }\\n    feed {\\n      id\\n      unread\\n      __typename\\n    }\\n    v2Preferred\\n    admin\\n    downloader\\n    publisherId\\n    hasAcceptedLatestTerms\\n    wishes\\n    lists {\\n      total\\n      results {\\n        ...list\\n        packageIds\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment list on List {\\n  id\\n  type\\n  listId\\n  slug\\n  name\\n  description\\n  ownerId\\n  ownerType\\n  status\\n  headerImage\\n  __typename\\n}\\n\",\"variables\":{\"id\":\"0\"},\"operationName\":\"CurrentUser\"},{\"query\":\"query ShoppingCartQuery {\\n  currentCart(namespace: \\\"asset_store_saved_cart\\\") {\\n    ...cartSimple\\n    __typename\\n  }\\n}\\n\\nfragment cartSimple on Cart {\\n  id\\n  items {\\n    id\\n    __typename\\n  }\\n  __typename\\n}\\n\",\"operationName\":\"ShoppingCartQuery\"},{\"query\":\"query ProductRatingStar {\\n  rating(id: $id) {\\n    count\\n    value\\n    __typename\\n  }\\n}\\n\",\"variables\":{\"id\":\"164532\"},\"operationName\":\"ProductRatingStar\"},{\"query\":\"query Publisher {\\n  publisher(id: $id) {\\n    id\\n    publisherProfileId\\n    organizationId\\n    name\\n    description\\n    website\\n    keyImages {\\n      type\\n      imageUrl\\n      __typename\\n    }\\n    supportUrl\\n    supportEmail\\n    shortUrl\\n    gaAccount\\n    gaPrefix\\n    packages(page: 1, size: 10) {\\n      total\\n      results {\\n        ...productQ\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment list on List {\\n  id\\n  type\\n  listId\\n  slug\\n  name\\n  description\\n  ownerId\\n  ownerType\\n  status\\n  headerImage\\n  __typename\\n}\\n\\nfragment product on Product {\\n  id\\n  productId\\n  itemId\\n  slug\\n  name\\n  description\\n  rating {\\n    average\\n    count\\n    __typename\\n  }\\n  currentVersion {\\n    id\\n    name\\n    publishedDate\\n    __typename\\n  }\\n  reviewCount\\n  downloadSize\\n  assetCount\\n  publisher {\\n    id\\n    name\\n    url\\n    supportUrl\\n    supportEmail\\n    gaAccount\\n    gaPrefix\\n    __typename\\n  }\\n  mainImage {\\n    big\\n    facebook\\n    small\\n    icon\\n    icon75\\n    __typename\\n  }\\n  originalPrice {\\n    itemId\\n    originalPrice\\n    finalPrice\\n    isFree\\n    discount {\\n      save\\n      percentage\\n      type\\n      saleType\\n      __typename\\n    }\\n    currency\\n    entitlementType\\n    __typename\\n  }\\n  images {\\n    type\\n    imageUrl\\n    thumbnailUrl\\n    __typename\\n  }\\n  category {\\n    id\\n    name\\n    slug\\n    longName\\n    __typename\\n  }\\n  firstPublishedDate\\n  publishNotes\\n  supportedUnityVersions\\n  state\\n  overlay\\n  overlayText\\n  popularTags {\\n    id\\n    pTagId\\n    name\\n    __typename\\n  }\\n  plusProSale\\n  licenseText\\n  __typename\\n}\\n\\nfragment productQ on ProductQ {\\n  id\\n  name\\n  rating {\\n    average\\n    count\\n    __typename\\n  }\\n  publisherName\\n  publisherId\\n  category\\n  mainImage\\n  iconImage\\n  price {\\n    price\\n    originPrice\\n    __typename\\n  }\\n  plusProSale\\n  onSale\\n  elevated\\n  url\\n  isNew\\n  partner\\n  __typename\\n}\\n\",\"variables\":{\"id\":\"5217\"},\"operationName\":\"Publisher\"},{\"query\":\"query ProductTags {\\n  product(id: $id) {\\n    id\\n    productId\\n    popularTags {\\n      id\\n      pTagId\\n      name\\n      __typename\\n    }\\n    userTags {\\n      id\\n      pTagId\\n      name\\n      type\\n      productId\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment product on Product {\\n  id\\n  productId\\n  itemId\\n  slug\\n  name\\n  description\\n  rating {\\n    average\\n    count\\n    __typename\\n  }\\n  currentVersion {\\n    id\\n    name\\n    publishedDate\\n    __typename\\n  }\\n  reviewCount\\n  downloadSize\\n  assetCount\\n  publisher {\\n    id\\n    name\\n    url\\n    supportUrl\\n    supportEmail\\n    gaAccount\\n    gaPrefix\\n    __typename\\n  }\\n  mainImage {\\n    big\\n    facebook\\n    small\\n    icon\\n    icon75\\n    __typename\\n  }\\n  originalPrice {\\n    itemId\\n    originalPrice\\n    finalPrice\\n    isFree\\n    discount {\\n      save\\n      percentage\\n      type\\n      saleType\\n      __typename\\n    }\\n    currency\\n    entitlementType\\n    __typename\\n  }\\n  images {\\n    type\\n    imageUrl\\n    thumbnailUrl\\n    __typename\\n  }\\n  category {\\n    id\\n    name\\n    slug\\n    longName\\n    __typename\\n  }\\n  firstPublishedDate\\n  publishNotes\\n  supportedUnityVersions\\n  state\\n  overlay\\n  overlayText\\n  popularTags {\\n    id\\n    pTagId\\n    name\\n    __typename\\n  }\\n  plusProSale\\n  licenseText\\n  __typename\\n}\\n\",\"variables\":{\"id\":\"164532\"},\"operationName\":\"ProductTags\"},{\"query\":\"mutation VisitProductDetailPage {\\n  visitProductDetailPage(id: $id) {\\n    packages\\n    __typename\\n  }\\n}\\n\",\"variables\":{\"id\":\"164532\"},\"operationName\":\"VisitProductDetailPage\"},{\"query\":\"query ProductMLRecommendation {\\n  product(id: $id) {\\n    id\\n    category {\\n      id\\n      name\\n      slug\\n      __typename\\n    }\\n    visualSimilarities(experiment: $experiment, variation: $variation, limit: 12, start: 0) {\\n      ...productCard\\n      __typename\\n    }\\n    boughtTogether(limit: 24, start: 0, fallback: true) {\\n      ...productCard\\n      __typename\\n    }\\n    mightAlsoLike(limit: 24, start: 0, fallback: false) {\\n      ...productCard\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment productCard on Product {\\n  id\\n  slug\\n  name\\n  rating {\\n    average\\n    count\\n    __typename\\n  }\\n  publisher {\\n    id\\n    name\\n    gaAccount\\n    gaPrefix\\n    __typename\\n  }\\n  mainImage {\\n    small\\n    icon\\n    __typename\\n  }\\n  originalPrice {\\n    itemId\\n    originalPrice\\n    finalPrice\\n    isFree\\n    discount {\\n      save\\n      percentage\\n      type\\n      saleType\\n      __typename\\n    }\\n    currency\\n    entitlementType\\n    __typename\\n  }\\n  category {\\n    id\\n    name\\n    slug\\n    longName\\n    __typename\\n  }\\n  state\\n  plusProSale\\n  currentVersion {\\n    publishedDate\\n    __typename\\n  }\\n  licenseText\\n  __typename\\n}\\n\",\"variables\":{\"id\":\"164532\",\"experiment\":\"\",\"variation\":\"\"},\"operationName\":\"ProductMLRecommendation\"},{\"query\":\"query PreviewAssets {\\n  product(id: $id) {\\n    id\\n    name\\n    assets(page: $page) {\\n      guid\\n      assetId: asset_id\\n      label\\n      level\\n      type\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\",\"variables\":{\"id\":\"164532\"},\"operationName\":\"PreviewAssets\"}]"
headers = {
    'authority': "assetstore.unity.com",
    'operations': "CurrentUser,ShoppingCartQuery,ProductRatingStar,Publisher,ProductTags,VisitProductDetailPage,ProductMLRecommendation,PreviewAssets",
    'x-csrf-token': csrf_token,
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    'content-type': "application/json;charset=UTF-8",
    'accept': "application/json, text/plain, */*",
    'sec-fetch-dest': "empty",
    'x-requested-with': "XMLHttpRequest",
    'origin': "https://assetstore.unity.com",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'referer': "https://assetstore.unity.com/",
    'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    'cookie': "_csrf=" + csrf_token,
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

# Your json data scraped from the api is in response.text
