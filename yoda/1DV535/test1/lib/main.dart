import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:geolocator/geolocator.dart';
import 'package:geocoding/geocoding.dart';
import 'package:intl/intl.dart';
import 'package:test1/providers/weather_provider.dart';

const Color kBackgroundColor = Colors.blueAccent;
String _cityName = 'Växjö';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => WeatherProvider(),
      child: MaterialApp(
        title: 'Weather App',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: const WeatherHomePage(),
      ),
    );
  }
}

class WeatherHomePage extends StatefulWidget {
  const WeatherHomePage({super.key});

  @override
  _WeatherHomePageState createState() => _WeatherHomePageState();
}

class _WeatherHomePageState extends State<WeatherHomePage> {
  int _currentIndex = 0;

  final List<Widget> _pages = [
    const WeatherHomePageContent(),
    const ForecastPage(),
    const AboutPage(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _pages[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home, color: Colors.black),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.calendar_today, color: Colors.black),
            label: 'Forecast',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.info, color: Colors.black),
            label: 'About',
          ),
        ],
      ),
    );
  }
}

class WeatherHomePageContent extends StatefulWidget {
  const WeatherHomePageContent({super.key});

  @override
  _WeatherHomePageContentState createState() => _WeatherHomePageContentState();
}

class _WeatherHomePageContentState extends State<WeatherHomePageContent> {
  final TextEditingController _cityController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _fetchLocationAndWeather();
  }

  Future<void> _fetchLocationAndWeather() async {
      Position position = await _getCurrentLocation();
      List<Placemark> placemarks = await placemarkFromCoordinates(position.latitude, position.longitude);
      Placemark placemark = placemarks.first;
      String cityName = placemark.locality ?? 'Växjö';

      setState(() {
        _cityName = cityName;
      });

      Provider.of<WeatherProvider>(context, listen: false).fetchWeather(_cityName);

  }

  Future<Position> _getCurrentLocation() async {
    bool serviceEnabled = await Geolocator.isLocationServiceEnabled();

    LocationPermission permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
    }

    return await Geolocator.getCurrentPosition();
  }

  @override
  Widget build(BuildContext context) {
    final weatherProvider = Provider.of<WeatherProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Weather App'),
      ),
      backgroundColor: kBackgroundColor,
      body: weatherProvider.currentWeather == null
          ? const Center(child: CircularProgressIndicator())
          : Center(
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Text(
                      '${weatherProvider.currentWeather?.cityName}',
                      style: Theme.of(context).textTheme.headlineMedium,
                    ),
                    if (weatherProvider.currentWeather?.icon != null)
                      Image.network(
                        'https://openweathermap.org/img/wn/${weatherProvider.currentWeather?.icon}@2x.png',
                      ),
                    Text(
                      '${weatherProvider.currentWeather?.temperature}°C',
                      style: Theme.of(context).textTheme.headlineSmall,
                    ),
                    Text(
                      '${weatherProvider.currentWeather?.description}',
                      style: Theme.of(context).textTheme.titleMedium,
                    ),
                  ],
                ),
              ),
            ),
    );
  }
}

class ForecastPage extends StatelessWidget {
  const ForecastPage({super.key});

  @override
  Widget build(BuildContext context) {
    final weatherProvider = Provider.of<WeatherProvider>(context);

    return Scaffold(
      body: weatherProvider.forecast == null
          ? const Center(child: CircularProgressIndicator())
          : Container(
              color: kBackgroundColor,
              child: ListView.builder(
                itemCount: weatherProvider.forecast?.forecasts.length ?? 0,
                itemBuilder: (context, index) {
                  final weather = weatherProvider.forecast?.forecasts[index];
                  final formattedTime = DateFormat('yyyy-MM-dd – HH:mm')
                      .format(weather?.time ?? DateTime.now());
                  return ListTile(
                    leading: Image.network(
                      'https://openweathermap.org/img/wn/${weather?.icon}@2x.png',
                    ),
                    title: Text('${weather?.temperature}°C'),
                    subtitle: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Text('${weather?.description}'),
                        Text('Time: $formattedTime'),
                      ],
                    ),
                  );
                },
              ),
            ),
    );
  }
}

class AboutPage extends StatelessWidget {
  const AboutPage({super.key});

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Center(
        child: Padding(
          padding: EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Text(
                'About',
                style: TextStyle(
                  fontSize: 24.0,
                  fontWeight: FontWeight.bold,
                  color: Colors.black,
                ),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 20.0),
              Text(
                'This is an app created for the course 1DV535 at LNU.',
                style: TextStyle(
                  fontSize: 18.0,
                  color: Colors.black87,
                ),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 10.0),
              Text(
                'Using Flutter and OpenWeather API',
                style: TextStyle(
                  fontSize: 16.0,
                  color: Colors.black54,
                ),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 20.0),
              Text(
                'Developed by William Schröder',
                style: TextStyle(
                  fontSize: 16.0,
                  fontWeight: FontWeight.bold,
                  color: Colors.black,
                ),
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
