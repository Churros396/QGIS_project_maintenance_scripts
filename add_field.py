# add a field to layers with a common prefix

# imports
from qgis.core import edit

# selecting Layers with the prefix
PFXs = []
# initializing layer tree
root = QgsProject.instance().layerTreeRoot()
#loop to fetch layer names meeting criterion
for layer in root.findLayers():
    print(layer.name())
    if 'PFX' in layer.name():
        PFXs.append(layer.name())
print(PFXs)
# adding the fields to the selected layers
for i in PFXs:
    # selecting the layer
    v = QgsProject.instance().mapLayersByName(i)
    vlayer = v[0]
    print(vlayer)
    # editing the layer and adding an integer Field
    with edit(vlayer):
        vlayer.addAttribute(QgsField('Fieldname', QVariant.Int))