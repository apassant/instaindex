# InstaIndex

Visually index your Instagram pictures, and find them in real-time!

InstaIndex is a simple pipeline combining Clarifai's image regognition / deep learning API and Algolia's search-as-a-service API to let you visually index your Instagram pictures, and find them in real-time!

## Pre-requisite

- Create an Clarifai application at http://www.clarifai.com/api
- Create an Instagram application at https://instagram.com/developer and generate an auth token
- Create an Algolia application and index at http://www.algolia.com/doc

## Tag and index data

The script to tag and index your Instagram pictures are located in ./scripts.

First, set-up virtualenv and install dependencies

    cd ./scripts
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Then, copy ./scripts/settings.py.dist into ./scripts/settings.py and update with your own values

    # Ignore pictures where the tagged concept has a probability below the threshold
    THRESHOLD = 0.9
    # Number of pictures to index
    MAX_MEDIA = 1000
    
    # Clarifai API details - http://www.clarifai.com/api
    CLARIFAI_APP_ID = 'xxx'
    CLARIFAI_APP_SECRET = 'xxx'
    
    # Instagram API details - https://instagram.com/developer
    # Get a token using instructions at https://instagram.com/developer/authentication/
    INSTAGRAM_API_KEY = 'xxx'
    INSTAGRAM_API_SECRET = 'xxx'
    INSTAGRAM_ACCESS_TOKEN = 'xxx'
    
    # Algolia API details = http://www.algolia.com/doc
    ALGOLIA_APP_ID = 'xxx'
    ALGOLIA_APP_KEY = 'xxx'
    ALGOLIA_INDEX_NAME = 'xxx'

Finally, launch the index procees

    python ./index.py

## Setup Algolia index

Go to the "Raking" page of your Algolia index settings and:
- Add (in this order) "likes", "tags", and "title" in "Basic settings" > "Custom ranking"
- Move "Custom" before "Attribute" in "Ranking formula" > "Ranking"

Go to the "Display" page of your Algolia index settings and:
- Add "tags" in "Faceting" > "Attributes for faceting"
- Add "tags", "created", "thumbnail", "title", "url", "likes" in "Display & Pagination" > "Attributes to retrieve"

## Web UI

A basic interface build on top of Algolia's instant-search is available in ./ui.

Edit ./ui/js/app.js to set-up your own Algolia API and index values

    // REPLACE WITH YOUR OWN VALUES
    var APPLICATION_ID = '8IOHDS4YN8';
    var SEARCH_ONLY_API_KEY = 'f7fe6cd7ccd1fc05b2f0074536c052d4';
    var INDEX_NAME = 'Pictures';
    var HITS_PER_PAGE = 25;
    var FACET_CONFIG = [{ 
        name: 'tags', 
        title: 'Tag', 
        disjunctive: false, 
        sortFunction: sortByCountDesc 
    }];
    var MAX_VALUES_PER_FACET = 10;
    // END REPLACE

