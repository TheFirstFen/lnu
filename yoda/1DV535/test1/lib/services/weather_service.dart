import 'dart:convert';
import 'package:http/http.dart' as http;

class WeatherService {
  final String apiKey = 'a35e81be6c08ffcfb11b36cdd7fc9952';
  final String baseUrl = 'https://api.openweathermap.org/data/2.5';

  Future<Map<String, dynamic>> getCurrentWeather(String cityName) async {
    final response = await http.get(
        Uri.parse('$baseUrl/weather?q=$cityName&units=metric&appid=$apiKey'));
    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load weather data');
    }
  }

  Future<Map<String, dynamic>> getForecast(String cityName) async {
    final response = await http.get(
        Uri.parse('$baseUrl/forecast?q=$cityName&units=metric&appid=$apiKey'));
    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load forecast data');
    }
  }
}
