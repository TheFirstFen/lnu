import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: MeCard(),
    );
  }
}

class MeCard extends StatelessWidget {
  const MeCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Personal Card'),
        backgroundColor: Colors.brown,
      ),
      backgroundColor: Colors.green[100],
      body: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ProfileImage(),
            SizedBox(height: 10),
            NameText(),
            SizedBox(height: 5),
            RoleText(),
            SizedBox(height: 20),
            InfoCard(
                icon: Icons.person,
                text: 'Han Solo',
                color: Colors.greenAccent),
            InfoCard(
                icon: Icons.language,
                text: 'Shyriiwook',
                color: Colors.lightGreen),
            InfoCard(icon: Icons.home, text: 'Kashyyyk', color: Colors.teal),
          ],
        ),
      ),
    );
  }
}

class ProfileImage extends StatelessWidget {
  const ProfileImage({super.key});

  @override
  Widget build(BuildContext context) {
    return const CircleAvatar(
      radius: 50,
      backgroundImage: AssetImage('assets/chewbacca.jpg'),
    );
  }
}

class NameText extends StatelessWidget {
  const NameText({super.key});

  @override
  Widget build(BuildContext context) {
    return Text(
      'Chewbacca',
      style: GoogleFonts.happyMonkey(
        fontSize: 30,
      ),
    );
  }
}

class RoleText extends StatelessWidget {
  const RoleText({super.key});

  @override
  Widget build(BuildContext context) {
    return const Text(
      'Co-pilot on the Millennium Falcon',
      style: TextStyle(
        fontSize: 16,
        fontWeight: FontWeight.bold,
        color: Color.fromARGB(255, 0, 0, 0),
      ),
    );
  }
}

class InfoCard extends StatelessWidget {
  final IconData icon;
  final String text;
  final Color color;

  const InfoCard({
    super.key,
    required this.icon,
    required this.text,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 20, vertical: 5),
      color: color, // Set the background color of the Card
      child: ListTile(
        leading: Icon(icon),
        title: Text(text),
      ),
    );
  }
}
