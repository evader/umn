
import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() => runApp(NebulaApp());

class NebulaApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'NebulaChat',
      home: Scaffold(
        appBar: AppBar(title: Text('NebulaChat')),
        body: WebView(
          initialUrl: 'https://your-web-app-link.com',
          javascriptMode: JavascriptMode.unrestricted,
        ),
      ),
    );
  }
}
