from .base import WEBSITE_UID

CATEGORY = [
    "sky", "beach", "flower", "rain", "forest", "sun", "night", "earth", 
    "sea", "water", "snow", "fire", "sunset", "smoke", "space", "clouds",
    "man", "girl", "sport", "music", "love", "party", "baby", 
    "woman", "couple", "business", "dance", "house", "family", "fashion",
    "cat", "monkey", "reptile", "zoo", "fish", "dog", "bird", "shark",
    "safari", "kitten", "wildlife", "tea", "corn", "cocktail", "eating", 
    "fast-food", "coffee", "fruit", "beer", "salad", "vegetable", "restaurant",
    "car", "city", "trains", "airplane", "bicycle", "drive", "street",
    "traffic", "trucks", "taxi", "motorcycle", "road"
]


CATEGORY_UID = {
    "sky": "01", "beach": "02", "flower": "03", "rain": "04", "forest": "05", 
    "sun": "06", "night": "07", "earth": "08", "sea": "09", "water": "10", 
    "snow": "11", "fire": "12", "sunset": "13", "smoke": "14", "space": "15", 
    "clouds": "16", "man": "17", "girl": "18", "sport": "19", "music": "20", 
    "love": "21", "party": "22", "baby": "23", "woman": "24", "couple": "25", 
    "business": "26", "dance": "27", "house": "28", "family": "29", "fashion": "30", 
    "cat": "31", "monkey": "32", "reptile": "33", "zoo": "34", "fish": "35", 
    "dog": "36", "bird": "37", "shark": "38", "safari": "39", "kitten": "40", 
    "wildlife": "41", "tea": "42", "corn": "43", "cocktail": "44", "eating": "45", 
    "fast-food": "46", "coffee": "47", "fruit": "48", "beer": "49", "salad": "50", 
    "vegetable": "51", "restaurant": "52", "car": "53", "city": "54", "trains": "55", 
    "airplane": "56", "bicycle": "57", "drive": "58", "street": "59", "traffic": "60", 
    "trucks": "61", "taxi": "62", "motorcycle": "63", "road": "64"
}


CATEGORY_PAGE_NUM = {'sky': 42, 'beach': 42, 'flower': 42, 'rain': 13, 'forest': 42, 
    'sun': 42, 'night': 42, 'earth': 13, 'sea': 42, 'water': 34, 'snow': 42, 'fire': 18, 
    'sunset': 42, 'smoke': 18, 'space': 19, 'clouds': 34, 'man': 34, 'girl': 67, 
    'sport': 42, 'music': 42, 'love': 36, 'party': 15, 'baby': 19, 'woman': 42, 
    'couple': 42, 'business': 42, 'dance': 42, 'house': 28, 'family': 25, 'fashion': 36, 
    'cat': 7, 'monkey': 16, 'reptile': 4, 'zoo': 7, 'fish': 10, 'dog': 19, 'bird': 21, 
    'shark': 1, 'safari': 3, 'kitten': 3, 'wildlife': 39, 'tea': 7, 'corn': 3, 'cocktail': 4, 
    'eating': 23, 'fast-food': 9, 'coffee': 26, 'fruit': 20, 'beer': 10, 'salad': 6, 
    'vegetable': 14, 'restaurant': 12, 'car': 42, 'city': 42, 'trains': 15, 'airplane': 13, 
    'bicycle': 19, 'drive': 3, 'street': 42, 'traffic': 67, 'trucks': 15, 'taxi': 3, 
    'motorcycle': 8, 'road': 42
}


def generate_mixkit_video_uid(
    category: str,
    page_idx: int,
    inner_idx: int,
    md5: str
) -> str:
    website_uid = WEBSITE_UID["mixkit"] # 2
    category_uid = CATEGORY_UID[category] # 2
    page_uid = "{:02d}".format(page_idx) # 2
    inner_uid = "{:02d}".format(inner_idx) # 2
    md5_uid = md5[:8] # 8
    video_uid = website_uid + category_uid + page_uid + inner_uid + md5_uid # 16
    return video_uid
    