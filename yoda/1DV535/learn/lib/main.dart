import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ToDo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSwatch().copyWith(
          primary: Color.fromRGBO(67, 235, 25, 0.612), // Change primary color
          secondary:
              Color.fromRGBO(67, 235, 25, 0.612), // Change secondary color
        ),
        useMaterial3: true,
      ),
      home: const ToDoPage(title: 'Add item to the ToDo'),
    );
  }
}

class ToDoPage extends StatefulWidget {
  const ToDoPage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  _ToDoPageState createState() => _ToDoPageState();
}

class _ToDoPageState extends State<ToDoPage> {
  final TextEditingController _controller = TextEditingController();
  List<String> _items = [];

  void _saveText() {
    setState(() {
      if (_controller.text.isNotEmpty) {
        _items.add(_controller.text);
        _controller.clear();
      }
    });
  }

  void _deleteText(String item) {
    setState(() {
      _items.remove(item);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor:
            Theme.of(context).colorScheme.primary, // Use primary color
        title: Text(widget.title),
      ),
      body: Padding(
        padding: const EdgeInsets.all(30.0),
        child: Column(
          children: <Widget>[
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Enter ToDo item',
                floatingLabelBehavior: FloatingLabelBehavior.always,
              ),
            ),
            ElevatedButton(
              onPressed: _saveText,
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: const [
                  Icon(Icons.add),
                  SizedBox(width: 5),
                  Text('Add item'),
                ],
              ),
            ),
            const SizedBox(height: 10),
            Expanded(
              child: ListView.builder(
                itemCount: _items.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Row(
                      children: [
                        Text(_items[index]),
                        const SizedBox(width: 30),
                        GestureDetector(
                          onTap: () => _deleteText(_items[index]),
                          child: Icon(Icons.delete),
                        ),
                      ],
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
