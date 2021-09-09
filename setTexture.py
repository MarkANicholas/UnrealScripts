import unreal
#running this script in unreal sets the parameters of selected textures.

#gets the selected assets and their data and stores them in variables
selctedAssets = unreal.EditorUtilityLibrary.get_selected_assets()
selctedAssetsData = unreal.EditorUtilityLibrary.get_selected_asset_data()

#method containing the settings to apply
def TextureSettings01(texture):
    texture.set_editor_property("sRGB", True)
    texture.set_editor_property("compression_no_alpha", True)
    texture.set_editor_property("adjust_brightness", 0.8)
    texture.set_editor_property("compression_settings", unreal.TextureCompressionSettings.TC_HDR_COMPRESSED)
    texture.set_editor_property("compression_quality", unreal.TextureCompressionQuality.TCQ_HIGH)
    
#iterate over each selected asset
for i, texture in enumerate(selctedAssets):
    #verify selected is a texture
    if selctedAssetsData[i].asset_class == 'Texture2D':
        #run the texture settings method
        TextureSettings01(texture)
    else:
        #print out selections that arnt a texture
        print("the following asset is not a texture: " + selctedAssetsData[i].asset_name)

#end of file
