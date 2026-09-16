# Hero Dex

Hero Dex is a Flutter application that displays information about different
superheroes in one place.

The app uses a local JSON file containing the superhero data. When the app
starts, the data is loaded and displayed as a list of heroes. A search option
is also provided to quickly find a particular hero.

## Features

- Displays a list of superheroes
- Shows information about each superhero
- Search superheroes by name
- Loads superhero data from a local JSON file
- Simple and responsive Flutter UI
- Can be run on an Android device or emulator

## How the App Works

The superhero information is stored in the `assets` folder in a file called
`superhero.json`.

When the application starts, Flutter reads this file using `rootBundle`.
The JSON data is then decoded and stored so that it can be displayed in the
application.

The main application logic is present in:

```text
lib/main.dart
```

The app first loads the superhero data. While the data is being loaded, a
loading indicator is displayed. Once the data is available, the superhero
list is shown.

The search functionality filters the loaded heroes based on the name entered
by the user.

### Important Files

**`lib/main.dart`**

Contains the main Flutter application code, including the UI, loading of
the JSON data, and search functionality.

**`assets/superhero.json`**

Contains the superhero information used by the application.

**`assets/hero_dex.png`**

Image used as the application icon.

**`pubspec.yaml`**

Contains the Flutter project configuration, dependencies, and asset
declarations.

## Technologies Used

- **Flutter** - Used to build the application.
- **Dart** - Programming language used for the Flutter code.
- **JSON** - Used to store the superhero data.

## Running the Project

Clone the repository and enter the project directory:

```bash
git clone https://github.com/777abhirup/amFOSS-Praveshan-2026/tree/main/Task-10
cd hero_dex
```

Get the Flutter dependencies:

```bash
flutter pub get
```

Check whether Flutter can detect the connected device:

```bash
flutter devices
```

Run the application:

```bash
flutter run
```

The application can be run on a physical Android device or an Android
emulator.

## JSON Data

The application does not require an internet connection to get the superhero
data.

The data is stored locally in:

```text
assets/superhero.json
```

This file is loaded when the application starts.

The JSON data contains the information required to display the superheroes
and their abilities.

## Search

The application includes a search field that makes it easier to find a
specific superhero.

When the user enters a name, the list is filtered and only the matching
heroes are displayed.

For example:

```text
Search: Spider-Man
```

The application will show the matching superhero instead of making the user
scroll through the complete list.

## Loading Data

The app uses Flutter's asset loading system to read the JSON file.

The basic flow is:

```text
Start App
   ↓
Load superhero.json
   ↓
Decode JSON
   ↓
Store superhero data
   ↓
Display heroes
```

While the JSON file is being loaded, the application displays a loading
indicator.

## Testing

The application was tested by running it on an Android device.

The following parts were checked:

- Application starts correctly
- Superhero data loads correctly
- Superhero list is displayed
- Search functionality works
- Different superhero names can be searched
- Application runs without crashing

## What I Learned

This project helped me understand the basics of building a Flutter
application.

Some of the things I learned are:

- How a Flutter project is structured
- How to create UI using Flutter widgets
- How to work with `StatefulWidget`
- How to load local assets
- How to read and decode JSON data
- How to display data using lists
- How to implement search functionality
- How to run and test a Flutter application on Android
- How to manage Flutter dependencies using `pubspec.yaml`

## Challenges

One of the important parts of the project was getting the local JSON data
to load correctly.

The JSON file has to be included as a Flutter asset in `pubspec.yaml`.
Without declaring the file as an asset, the application cannot load it
using `rootBundle`.

The asset configuration includes:

```yaml
flutter:
  uses-material-design: true
  assets:
    - assets/hero_dex.png
    - assets/superhero.json
```

## Final Result

Hero Dex provides a simple way to browse and search through the superhero
data using a Flutter application.

The project also gave me practical experience with Flutter UI development,
local data handling, JSON parsing, and running an Android application.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Learn Flutter](https://docs.flutter.dev/get-started/learn-flutter)
- [Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Flutter learning resources](https://docs.flutter.dev/reference/learning-resources)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.