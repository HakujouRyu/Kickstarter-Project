import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from joblib import load
from xgboost import XGBClassifier
import pandas as pd
from datetime import datetime as dt

pipeline = load('assets/pipeline.joblib')
#['country', 'goal', 'month_started', 'year_started', 'month_launched',
# 'day_launched', 'year_launched', 'deadline_month', 'deadline_year', 
#'days_to_launch', 'campaign_length', 'category_name']

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Country'), 
        dcc.Dropdown(
            id='country',
            options= [
                {'label': 'US', 'value': 'US'},
                {'label': 'GB', 'value': 'GB'}, 
                {'label': 'CA', 'value': 'CA'}, 
                {'label': 'AU', 'value': 'AU'}, 
                {'label': 'DE', 'value': 'DE'}, 
                {'label': 'FR', 'value': 'FR'}, 
                {'label': 'IT', 'value': 'IT'}, 
                {'label': 'NL', 'value': 'NL'}, 
                {'label': 'MX', 'value': 'MX'}, 
                {'label': 'ES', 'value': 'ES'}, 
                {'label': 'SE', 'value': 'SE'}, 
                {'label': 'NZ', 'value': 'NZ'}, 
                {'label': 'DK', 'value': 'DK'}, 
                {'label': 'IE', 'value': 'IE'}, 
                {'label': 'HK', 'value': 'HK'}, 
                {'label': 'CH', 'value': 'CH'}, 
                {'label': 'SG', 'value': 'SG'}, 
                {'label': 'NO', 'value': 'NO'}, 
                {'label': 'BE', 'value': 'BE'}, 
                {'label': 'AT', 'value': 'AT'}, 
                {'label': 'JP', 'value': 'JP'}, 
                {'label': 'LU', 'value': 'LU'}
                ],
            className='mb-5', 
        ), 
        dcc.Markdown('#### Goal'), 
        daq.Knob(
            id='goal',
            value=1000,
            min=0,
            max=100000,
            className='mb-5',
        ),  
        dcc.DatePickerSingle(
            id='launch',
            placeholder="Created Date",
            className='mb-5',
        ) ,
        dcc.DatePickerSingle(
            id='launch',
            placeholder="Launch Date",
            className='mb-5',
        ),
        dcc.DatePickerSingle(
            id='deadline',
            placeholder="Deadline",
            className='mb-5',
        ),    
        dcc.Dropdown(
            id='Category',
            placeholder='Category',
            options= [
                {'label': '3D Printing', 'value': '3D Printing'}, 
                {'label': 'Academic', 'value': 'Academic'}, 
                {'label': 'Accessories', 'value': 'Accessories'}, 
                {'label': 'Action', 'value': 'Action'}, 
                {'label': 'Animals', 'value': 'Animals'}, 
                {'label': 'Animation', 'value': 'Animation'},
                {'label': 'Anthologies', 'value': 'Anthologies'}, 
                {'label': 'Apparel', 'value': 'Apparel'}, 
                {'label': 'Apps', 'value': 'Apps'}, 
                {'label': 'Architecture', 'value': 'Architecture'}, 
                {'label': 'Art', 'value': 'Art'}, 
                {'label': 'Art Books', 'value': 'Art Books'}, 
                {'label': 'Audio', 'value': 'Audio'}, 
                {'label': 'Bacon', 'value': 'Bacon'}, 
                {'label': 'Blues', 'value': 'Blues'}, 
                {'label': 'Calendars', 'value': 'Calendars'}, 
                {'label': 'Camera Equipment', 'value': 'Camera Equipment'}, 
                {'label': 'Candles', 'value': 'Candles'}, 
                {'label': 'Ceramics', 'value': 'Ceramics'}, 
                {'label': "Children's Books", 'value': "Children's Books"}, 
                {'label': 'Childrenswear', 'value': 'Childrenswear'}, 
                {'label': 'Chiptune', 'value': 'Chiptune'}, 
                {'label': 'Civic Design', 'value': 'Civic Design'}, 
                {'label': 'Classical Music', 'value': 'Classical Music'}, 
                {'label': 'Comedy', 'value': 'Comedy'}, 
                {'label': 'Comic Books', 'value': 'Comic Books'}, 
                {'label': 'Comics', 'value': 'Comics'}, 
                {'label': 'Community Gardens', 'value': 'Community Gardens'}, 
                {'label': 'Conceptual Art', 'value': 'Conceptual Art'}, 
                {'label': 'Cookbooks', 'value': 'Cookbooks'}, 
                {'label': 'Country & Folk', 'value': 'Country & Folk'}, 
                {'label': 'Couture', 'value': 'Couture'}, 
                {'label': 'Crafts', 'value': 'Crafts'}, 
                {'label': 'Crochet', 'value': 'Crochet'}, 
                {'label': 'DIY', 'value': 'DIY'}, 
                {'label': 'DIY Electronics', 'value': 'DIY Electronics'}, 
                {'label': 'Dance', 'value': 'Dance'}, 
                {'label': 'Design', 'value': 'Design'}, 
                {'label': 'Digital Art', 'value': 'Digital Art'}, 
                {'label': 'Documentary', 'value': 'Documentary'}, 
                {'label': 'Drama', 'value': 'Drama'}, 
                {'label': 'Drinks', 'value': 'Drinks'}, 
                {'label': 'Electronic Music', 'value': 'Electronic Music'}, 
                {'label': 'Embroidery', 'value': 'Embroidery'}, 
                {'label': 'Events', 'value': 'Events'}, 
                {'label': 'Experimental', 'value': 'Experimental'}, 
                {'label': 'Fabrication Tools', 'value': 'Fabrication Tools'}, 
                {'label': 'Faith', 'value': 'Faith'}, 
                {'label': 'Family', 'value': 'Family'}, 
                {'label': 'Fantasy', 'value': 'Fantasy'}, 
                {'label': "Farmer's Markets", 'value': "Farmer's Markets"}, 
                {'label': 'Farms', 'value': 'Farms'}, 
                {'label': 'Fashion', 'value': 'Fashion'}, 
                {'label': 'Festivals', 'value': 'Festivals'}, 
                {'label': 'Fiction', 'value': 'Fiction'}, 
                {'label': 'Film & Video', 'value': 'Film & Video'}, 
                {'label': 'Fine Art', 'value': 'Fine Art'}, 
                {'label': 'Flight', 'value': 'Flight'}, 
                {'label': 'Food', 'value': 'Food'}, 
                {'label': 'Food Trucks', 'value': 'Food Trucks'}, 
                {'label': 'Footwear', 'value': 'Footwear'}, 
                {'label': 'Gadgets', 'value': 'Gadgets'}, 
                {'label': 'Games', 'value': 'Games'}, 
                {'label': 'Gaming Hardware', 'value': 'Gaming Hardware'}, 
                {'label': 'Glass', 'value': 'Glass'}, 
                {'label': 'Graphic Design', 'value': 'Graphic Design'}, 
                {'label': 'Graphic Novels', 'value': 'Graphic Novels'}, 
                {'label': 'Hardware', 'value': 'Hardware'}, 
                {'label': 'Hip-Hop', 'value': 'Hip-Hop'}, 
                {'label': 'Horror', 'value': 'Horror'}, 
                {'label': 'Illustration', 'value': 'Illustration'}, 
                {'label': 'Immersive', 'value': 'Immersive'}, 
                {'label': 'Indie Rock', 'value': 'Indie Rock'}, 
                {'label': 'Installations', 'value': 'Installations'}, 
                {'label': 'Interactive Design', 'value': 'Interactive Design'}, 
                {'label': 'Jazz', 'value': 'Jazz'}, {'label': 'Jewelry', 'value': 'Jewelry'}, 
                {'label': 'Journalism', 'value': 'Journalism'}, {'label': 'Kids', 'value': 'Kids'}, 
                {'label': 'Knitting', 'value': 'Knitting'}, {'label': 'Latin', 'value': 'Latin'}, 
                {'label': 'Letterpress', 'value': 'Letterpress'}, 
                {'label': 'Literary Journals', 'value': 'Literary Journals'}, 
                {'label': 'Literary Spaces', 'value': 'Literary Spaces'}, 
                {'label': 'Live Games', 'value': 'Live Games'}, 
                {'label': 'Makerspaces', 'value': 'Makerspaces'}, {'label': 'Metal', 'value': 'Metal'},
                {'label': 'Mixed Media', 'value': 'Mixed Media'}, 
                {'label': 'Mobile Games', 'value': 'Mobile Games'}, 
                {'label': 'Movie Theaters', 'value': 'Movie Theaters'}, 
                {'label': 'Music', 'value': 'Music'}, {'label': 'Music Videos', 'value': 'Music Videos'}, 
                {'label': 'Musical', 'value': 'Musical'}, 
                {'label': 'Narrative Film', 'value': 'Narrative Film'}, 
                {'label': 'Nature', 'value': 'Nature'}, {'label': 'Nonfiction', 'value': 'Nonfiction'}, 
                {'label': 'Painting', 'value': 'Painting'}, {'label': 'People', 'value': 'People'}, 
                {'label': 'Performance Art', 'value': 'Performance Art'}, 
                {'label': 'Performances', 'value': 'Performances'}, 
                {'label': 'Periodicals', 'value': 'Periodicals'}, 
                {'label': 'Pet Fashion', 'value': 'Pet Fashion'}, {'label': 'Photo', 'value': 'Photo'}, 
                {'label': 'Photobooks', 'value': 'Photobooks'}, 
                {'label': 'Photography', 'value': 'Photography'}, {'label': 'Places', 'value': 'Places'}, 
                {'label': 'Playing Cards', 'value': 'Playing Cards'}, {'label': 'Plays', 'value': 'Plays'}, 
                {'label': 'Poetry', 'value': 'Poetry'}, {'label': 'Pop', 'value': 'Pop'}, 
                {'label': 'Pottery', 'value': 'Pottery'}, {'label': 'Print', 'value': 'Print'}, 
                {'label': 'Printing', 'value': 'Printing'}, 
                {'label': 'Product Design', 'value': 'Product Design'}, 
                {'label': 'Public Art', 'value': 'Public Art'}, {'label': 'Publishing', 'value': 'Publishing'}, 
                {'label': 'Punk', 'value': 'Punk'}, {'label': 'Puzzles', 'value': 'Puzzles'}, 
                {'label': 'Quilts', 'value': 'Quilts'}, {'label': 'R&B', 'value': 'R&B'}, 
                {'label': 'Radio & Podcasts', 'value': 'Radio & Podcasts'}, 
                {'label': 'Ready-to-wear', 'value': 'Ready-to-wear'}, 
                {'label': 'Residencies', 'value': 'Residencies'}, 
                {'label': 'Restaurants', 'value': 'Restaurants'}, {'label': 'Robots', 'value': 'Robots'}, 
                {'label': 'Rock', 'value': 'Rock'}, {'label': 'Romance', 'value': 'Romance'}, 
                {'label': 'Science Fiction', 'value': 'Science Fiction'}, 
                {'label': 'Sculpture', 'value': 'Sculpture'}, {'label': 'Shorts', 'value': 'Shorts'}, 
                {'label': 'Small Batch', 'value': 'Small Batch'}, {'label': 'Software', 'value': 'Software'}, 
                {'label': 'Sound', 'value': 'Sound'}, 
                {'label': 'Space Exploration', 'value': 'Space Exploration'}, 
                {'label': 'Spaces', 'value': 'Spaces'}, {'label': 'Stationery', 'value': 'Stationery'}, 
                {'label': 'Tabletop Games', 'value': 'Tabletop Games'}, 
                {'label': 'Taxidermy', 'value': 'Taxidermy'}, {'label': 'Technology', 'value': 'Technology'}, 
                {'label': 'Television', 'value': 'Television'}, {'label': 'Textiles', 'value': 'Textiles'}, 
                {'label': 'Theater', 'value': 'Theater'}, {'label': 'Thrillers', 'value': 'Thrillers'}, 
                {'label': 'Translations', 'value': 'Translations'},
                {'label': 'Typography', 'value': 'Typography'}, 
                {'label': 'Vegan', 'value': 'Vegan'}, {'label': 'Video', 'value': 'Video'}, 
                {'label': 'Video Art', 'value': 'Video Art'}, {'label': 'Video Games', 'value': 'Video Games'}, 
                {'label': 'Wearables', 'value': 'Wearables'}, {'label': 'Weaving', 'value': 'Weaving'}, 
                {'label': 'Web', 'value': 'Web'}, {'label': 'Webcomics', 'value': 'Webcomics'}, 
                {'label': 'Webseries', 'value': 'Webseries'}, 
                {'label': 'Woodworking', 'value': 'Woodworking'}, 
                {'label': 'Workshops', 'value': 'Workshops'},
                {'label': 'World Music', 'value': 'World Music'}, 
                {'label': 'Young Adult', 'value': 'Young Adult'}, 
                {'label': 'Zines', 'value': 'Zines'}
                ],
            className='mb-5', 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [


    ]
)
column3 = dbc.Col(
    [
        html.H2('Expected Lifespan', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2, column3] )

@app.callback(
    Output('prediction-content', 'children'),
    [Input('year', 'value'), Input('continent', 'value')],
)
def predict(year, continent):
    df = pd.DataFrame(
        columns=['year', 'continent'], 
        data=[[year, continent]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} years'