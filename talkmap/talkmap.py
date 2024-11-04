# import pygal
import pygal
  
# import Style class from pygal.style
from pygal.style import Style
  
# create a Style object
custom_style = Style(background='#fafafa',
			plot_background='#fafafa',
			font_family='sans-serif')
  
# create a world map,
# Style class is used for using
# the custom colours in the map,
worldmap =  pygal.maps.world.World(style = custom_style, show_legend=False)

#####################
# updated on Nov 2024

# ca: 23.02, 23.02, 23.02, 23.10				= 4
# de: 23.05, 24.09						= 2
# es: 22.12, 23.09						= 2
# jp: 22.09, 22.09, 22.09, 23.06, 24.10, 24.11		= 6
#####################
  
# adding the countries
worldmap.add('talks', {
        'ca' : 4,
        'de' : 2,
        'es' : 2,
        'jp' : 6
})
  
# save into the file
worldmap.render_in_browser()
  
print("Success")
