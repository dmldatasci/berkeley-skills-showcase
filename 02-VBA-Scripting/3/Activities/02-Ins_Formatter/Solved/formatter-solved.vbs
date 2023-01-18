Sub formatter()

  ' Set the Font colour to Red
  Range("A1").Font.ColorIndex = 3

  ' Set the Cell Colours to Red
  Range("A2:A5").Interior.ColorIndex = 3

  ' Set the Font Colour to Green
  Range("B1").Font.ColorIndex = 4

  ' Set the Cell Colours to Green
  Range("B2:B5").Interior.ColorIndex = 4

  ' Set the Colour Index to Blue
  Range("C1").Font.ColorIndex = 5

  ' Set the Cell Colours to Blue
  Range("C2:C5").Interior.ColorIndex = 5

  ' Set the Colour Index to Magenta
  Range("D1").Font.ColorIndex = 7

  ' Set the Cell Colours to Magenta
  Range("D2:D5").Interior.ColorIndex = 7

  ' See this website for color guides: http://dmcritchie.mvps.org/excel/colors.htm
End Sub
