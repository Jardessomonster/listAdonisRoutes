import os
import re
import openpyxl
import treatingRouteFile as Route


modules = {
    'social-network': '../incicle/social-media/back-social-media',
    'core': '../incicle/core/core-backend'
}

route = Route.treatingTheFile(modules['social-network'], 'social-network')

print(route.creatingRouteFile())