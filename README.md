# Action Theme for Notepad++

*Action* is a high-visibility dark theme and simplified themeing system for Notepad++.

This theme came about as a result of my disappointment with the readability of most dark themes for text editors.  Many themes are beautiful and nicely color matched but ultimately lack adequate contrast for me to read the text easily.  The colors in *Action* are very bright against a nearly black background, and all colors are selected from a 12-hue rainbow distributed evenly across the RGB spectrum.

The color scheme is mostly based on the Notepad++ default theme and VS Dark.

## Simplified Styling System

The Notepad++ stylers system includes over 1800 lines of settings in XML, each requiring one or two RGB color codes.  *Action* comes with tooling that simplifies color themes down to about 100 settings, half of which are UI colors and the other half language syntax colors.  This simplified set is then applied to all the languages that Notepad++ supports.  This process reduces the flexibility of the theme somewhat, but also automatically standardizes the theme across languages.  In addition, the tool allow the definition of color names to make themes easier to work with.

The stylers generation tool includes a stylers XML template which is based on `stylers.model.xml` that comes with the default Notepad++ install.  Themes are defined in straightforward JSON files.  A simple Python script generates the `Action.xml` file.