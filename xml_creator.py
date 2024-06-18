#Input files path/names
in_back = 'in-back.txt'
in_front = 'in-front.txt'

#XML
xml_header = '''<deck name="Title">
  <fields>
    <japanese name='Japanese' sides='11' furiganaMode='hint'></japanese>
    <text name='Meaning' sides='01' lang='pl-PL'>
      <sources>
        <translation>
          <ref name="Japanese" />
        </translation>
      </sources>
    </text>
  </fields>
  <cards>
'''

xml_content = '''    <card>
      <field name='Japanese'>
        <japanese>Card_Front</japanese>
      </field>
      <field name='Meaning'>Card_Back</field>
    </card>
'''

xml_footer = '''  </cards>
</deck>'''

#Custom Exceptions
class NotSameLineNumber(Exception):
    "Raised when input files dont have the same line number"
    pass


try:
  with open(in_back, 'r' , encoding='UTF-8') as input_back_file:
    with open(in_front, 'r' , encoding='UTF-8') as input_front_file:

      #Check NotSameLineNumber Exceptions
      line_in_file_number = sum(1 for _ in input_back_file)
      if line_in_file_number == sum(1 for _ in input_front_file):
        
        #Reset files position
        input_back_file.seek(0,0)
        input_front_file.seek(0,0)

        #Create xml file
        with open('___.xml', 'w', encoding='UTF-8') as output_file:
          newTitle = input('Enter the name of the deck:')

          output_file.write(xml_header.replace('Title', newTitle))

          for line_number in range(0, line_in_file_number):
            #Read line from files
            front_line = input_front_file.readline()
            back_line = input_back_file.readline()

            #Prepare new card
            new_card = xml_content

            new_card = new_card.replace('Card_Front', front_line.strip())
            new_card = new_card.replace('Card_Back', back_line.strip())

            #Write new card
            output_file.write(new_card)

          output_file.write(xml_footer)
      else:
        raise NotSameLineNumber
except FileNotFoundError as error:
  print(f"Not found {error.filename} file.")
except NotSameLineNumber:
  print("Input files dont have the same line number.")