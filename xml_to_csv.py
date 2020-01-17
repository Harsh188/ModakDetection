import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
	#this method will use the path way to the xml file
	#inorder to conver the xml file to csv
    xml_list = []
    #we loop through all of the xml files in the folder
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            #we append all of the features to the xml_list
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    #finally we use pandas to convert the xml to a data frame
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
	#loop through all of the images in the train and test folder under images
    for folder in ['train','test']:
    	#go to the images folder
        image_path = os.path.join(os.getcwd(), ('images/' + folder))
        #convert all of the files to csv
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')


main()