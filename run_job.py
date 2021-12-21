
# python3

import os
import io
import json
import traceback

def detect_toponyms(url, text_options=None, toponym_options=None):
    # download image to temporary location
    #from urllib.request import urlretrieve
    #path = urlretrieve(url)
    #print(path)

    # open image
    from PIL import Image
    from urllib.request import urlopen
    fobj = io.BytesIO(urlopen(url).read())
    im = Image.open(fobj)
    print(im)

    # detect map text
    import maponyms
    kwargs = text_options or {}
    if 'textcolor' not in kwargs: 
        kwargs['textcolor'] = (0,0,0)
    textdata = maponyms.main.text_detection(im, **kwargs)

    # select toponym candidates
    kwargs = toponym_options or {}
    candidate_toponyms = maponyms.main.toponym_selection(im, textdata, **kwargs)
    return candidate_toponyms

def match_toponyms(toponyms, **match_options):
    import maponyms

    # find toponym coordinates
    db = r"C:\Users\kimok\Desktop\gazetteers\new\gazetteers.db"
    matched_toponyms = maponyms.main.match_control_points(toponyms, db=db, **match_options)

    # make into control points
    return matched_toponyms

def estimate_transform(controlpoints, **transform_options):
    import transformio as tio

    # format the control points as expected by transformio
    frompoints = [(feat['properties']['origx'],feat['properties']['origy']) for feat in controlpoints['features']]
    topoints = [(feat['properties']['matchx'],feat['properties']['matchy']) for feat in controlpoints['features']]
    fromx,fromy = zip(*frompoints)
    tox,toy = zip(*topoints)

    # estimate the transform
    trans = tio.transforms.Polynomial()
    trans.fit(fromx, fromy, tox, toy)
    transdata = trans.to_json()
    
    return transdata

def full_auto(url, text_options=None, toponym_options=None, match_options=None, transform_options=None):
    toponyms = detect_toponyms(url, text_options, toponym_options)
    matched = match_toponyms(toponyms, **match_options or {})
    transform = estimate_transform(matched, **transform_options or {})
    return toponyms,matched,transform

def post_toponyms(toponyms):
    print('posting toponyms')

def post_transform(toponyms):
    print('posting transform')

#####################################

def run_action(action, **kwargs):
    # call the correct function
    # upon completion, should submit/add the data to the maplocate website
    # NOT FINISHED
    # ... 
    result = {}
    try:
        if action == 'detect_toponyms':
            # get results
            toponyms = detect_toponyms(**kwargs)
            print(toponyms)
            # post toponyms
            # ...

        elif action == 'match_toponyms':
            # get results
            matched = match_toponyms(**kwargs)
            print(matched)
            # post matches
            # ...

        elif action == 'estimate_transform':
            # get results
            transform = estimate_transform(**kwargs)
            print(transform)
            # post transform
            # ...

        elif action == 'full_auto':
            # get results
            results = full_auto(**kwargs)
            print(results)
            # post matches
            # ...

    except:
        err = traceback.format_exc()
        print('ERROR:', err)

if __name__ == '__main__':
    # this part gets executed when a job is run

    # get input data as json dict passed through environment variable
    data = json.loads(os.environ['MAPLOCATE_INPUT'])
    #data = {'action':'full_auto', 
    #        'data': {
    #            'url': 'https://legacy.lib.utexas.edu/maps/africa/south_africa_pol_2005.jpg',
    #            }
    #        }

    # run the action
    run_action(data['action'], **data['data'])





    

