import os
import re
import openpyxl
import treatingRouteFile as Route


modules = {
    'social-network': '../incicle/social-media/back-social-media',
    'core': '../incicle/core/core-backend'
}

routeSocialMedia = Route.treatingTheFile(modules['social-network'], 'social-network')
routeCore = Route.treatingTheFile(modules['core'], 'core')

routeSocialMedia.creatingRouteFile()
routeCore.creatingRouteFile()