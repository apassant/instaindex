from instaindex import InstaIndex

from settings import INSTAGRAM_API_SECRET, INSTAGRAM_ACCESS_TOKEN
from settings import CLARIFAI_APP_ID, CLARIFAI_APP_SECRET
from settings import ALGOLIA_APP_ID, ALGOLIA_APP_KEY, ALGOLIA_INDEX_NAME
from settings import THRESHOLD, MAX_MEDIA

if __name__ == "__main__" :
    index = InstaIndex(
        INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_API_SECRET, 
        CLARIFAI_APP_ID, CLARIFAI_APP_SECRET,
        ALGOLIA_APP_ID, ALGOLIA_APP_KEY, ALGOLIA_INDEX_NAME,
        THRESHOLD, MAX_MEDIA
    )
    index.run()