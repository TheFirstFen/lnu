class Weather {
  final String description;
  final double temperature;
  final String cityName;
  final String icon;
  final DateTime time;

  Weather({
    required this.description,
    required this.temperature,
    required this.cityName,
    required this.icon,
    required this.time,
  });

  factory Weather.fromJson(Map<String, dynamic> json) {
    DateTime time = DateTime.fromMillisecondsSinceEpoch(json['dt'] * 1000);

    return Weather(
      description: json['weather'][0]['description'],
      temperature: json['main']['temp'].toDouble(),
      cityName: json['name'],
      icon: json['weather'][0]['icon'],
      time: time,
    );
  }
}

class Forecast {
  final List<Weather> forecasts;

  Forecast({required this.forecasts});

  factory Forecast.fromJson(Map<String, dynamic> json) {
    List<Weather> forecasts = [];
    for (var item in json['list']) {
      DateTime time = DateTime.fromMillisecondsSinceEpoch(item['dt'] * 1000);

      forecasts.add(Weather(
        description: item['weather'][0]['description'],
        temperature: item['main']['temp'].toDouble(),
        cityName: json['city']['name'],
        icon: item['weather'][0]['icon'],
        time: time,
      ));
    }
    return Forecast(forecasts: forecasts);
  }
}
