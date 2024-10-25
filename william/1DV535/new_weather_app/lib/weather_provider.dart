import 'package:flutter/material.dart';
import 'package:new_weather_app/weather.dart';
import 'package:new_weather_app/weather_service.dart';

class WeatherProvider with ChangeNotifier {
  final WeatherService _weatherService = WeatherService();
  Weather? currentWeather;
  Forecast? forecast;

  Future<void> fetchWeather(String cityName) async {
    try {
      currentWeather = Weather.fromJson(await _weatherService.getCurrentWeather(cityName));
      forecast = Forecast.fromJson(await _weatherService.getForecast(cityName));
      notifyListeners();
    } catch (e) {
      print("Error fetching weather data: $e");
    }
  }
}
