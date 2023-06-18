# this script updates the value map of multiple layers with the same prefix based on an excel file
# the excel file was previously imported as layer

# create a list of the layers via a common prefix

#empty List
Ls = []
# initialise layer tree
root = QgsProject.instance().layerTreeRoot()
# loop through layers
for layer in root.findLayers():
    if 'A' in layer.name():
        print(layer.name())
        PFXs.append(layer.name())

# see the list of all the selected layers
print(PFXs)

# create the value map

# selecting the excel layer to a list
layers = QgsProject.instance().mapLayersByName('Excellayer')
# selecting an elements from the list
a = layers[0]
# check the selected layer name and type
print(a.name(),"is a ",a.type())

# extracting the entries from the excel, for every value and description an dictionary is created

# list for the created dictionairies
value_pairs = []
# acces feature attributes
for feature in a.getFeatures():
    attrs = feature.attributes() # do something with feature
    f = {}
    f[attrs[1]] = attrs[0] # creating the dictionary entry
    # create dictionay list
    value_pairs.append(f)
print(value_pairs)
# combine to a value map like v_map= {'map':[liste]}
v_map = {'map':value_pairs}
print("Value Map:", v_map)

# load value map for a field via the field index

# list of fields where value map will be applied
u_fields = ['Fieldname_1']
# looping selected Layers by their names
for i in PFXs:
    layers = QgsProject.instance().mapLayersByName(i)
    PFX = layers[0]
    print(PFX.name())

    # looping fields from list
    for i in u_fields:
        # get index of the field to be updated
        fld_idx = PFX.fields().lookupField(i)        PFX.setEditorWidgetSetup(fld_idx, QgsEditorWidgetSetup('ValueMap', v_map))