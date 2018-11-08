# Customization of PP website

This is the Plone customization of the PP website.


## Personality Test

1. Add a PFG form

2. Action "Eigene Erfolgsaktion" needs to point to `traverse_to:string:string:evaluate`

3. Fields Ids need to be `['kontakt', 'empfindung', 'stimme', 'sprache', 'koerper', 'erscheinung']`

4. Add a Python Script in ZMI with the ID `text_detail_elements`. Return a dictionary of this style:

  ```python
    
  elements = {
      'sprache': {
          '1': {
              'Meistens': '',
              'Manchmal': 'A text',
              'Selten':  'Another text',
              'Nie': 'Yet another text',
              'default': 'Nicht ausgefüllt',
              'Titel': 'Verständlichkeit',
          }, 
      }
  }
  ```
  
  All the keys of 3. need to be present. 

5. Add a Python Script in ZMI with the ID `text_summary_elements`. Return a dictionary of this style:

   ```python
   
   {
       'bad': 'Bad summary',
       'med': 'Med summary',
       'good': 'Good summary'
   }
   ```
   The hard coded threshold for the texts is BAD < 20 (MED) < 90 (GOOD)
   
   