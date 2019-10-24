import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## You're building it...
            ### But will they come?
            
            Kickstarter has become an incredibly popular platform for all types of creators.  
            Since it's beginning, Kickstarter has seen over 57M pledges across more than 464,000 projects!
            with Kickstarter pulling in well over $4.6B spanning 171,000+ projects, it really is easy to see why so many
            companies and entrepreneurs flock to this platform to find their success story.

            Here is a web app I've created to help you on your journey. Just fill in the information on your project and let's see what the data has to say
            on your projects' survival.

            """
        ),
        dcc.Link(dbc.Button('Find out now!', color='success'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])