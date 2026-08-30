import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() {
  runApp(const HeroDexApp());
}

class HeroDexApp extends StatelessWidget {
  const HeroDexApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Hero Dex',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const HeroListPage(),
    );
  }
}

class HeroListPage extends StatefulWidget {
  const HeroListPage({super.key});

  @override
  State<HeroListPage> createState() => _HeroListPageState();
}

class _HeroListPageState extends State<HeroListPage> {
  List<dynamic> heroes = [];
  List<dynamic> filteredHeroes = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    loadHeroes();
  }

  Future<void> loadHeroes() async {
    final String data =
        await rootBundle.loadString('assets/superhero.json');

    final decodedData = json.decode(data);

    setState(() {
      heroes = decodedData is List ? decodedData : decodedData['heroes'];
      filteredHeroes = heroes;
      isLoading = false;
    });
  }

  void searchHeroes(String query) {
    setState(() {
      filteredHeroes = heroes.where((hero) {
        final name =
            (hero['name'] ?? hero['Name'] ?? '').toString().toLowerCase();

        return name.contains(query.toLowerCase());
      }).toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          '🦸 HERO DEX',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
      ),
      body: isLoading
          ? const Center(child: CircularProgressIndicator())
          : Column(
              children: [
                Padding(
                  padding: const EdgeInsets.all(12),
                  child: TextField(
                    onChanged: searchHeroes,
                    decoration: InputDecoration(
                      hintText: 'Search superhero...',
                      prefixIcon: const Icon(Icons.search),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(15),
                      ),
                    ),
                  ),
                ),
                Expanded(
                  child: ListView.builder(
                    itemCount: filteredHeroes.length,
                    itemBuilder: (context, index) {
                      final hero = filteredHeroes[index];

                      final name =
                          hero['name'] ?? hero['Name'] ?? 'Unknown Hero';

                      return Card(
                        margin: const EdgeInsets.symmetric(
                          horizontal: 12,
                          vertical: 6,
                        ),
                        child: ListTile(
                          leading: const CircleAvatar(
                            child: Icon(Icons.person),
                          ),
                          title: Text(
                            name.toString(),
                            style: const TextStyle(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          trailing:
                              const Icon(Icons.arrow_forward_ios),
                          onTap: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) =>
                                    HeroDetailsPage(hero: hero),
                              ),
                            );
                          },
                        ),
                      );
                    },
                  ),
                ),
              ],
            ),
    );
  }
}

class HeroDetailsPage extends StatelessWidget {
  final dynamic hero;

  const HeroDetailsPage({
    super.key,
    required this.hero,
  });

  @override
  Widget build(BuildContext context) {
    final name = hero['name'] ?? hero['Name'] ?? 'Unknown Hero';

    return Scaffold(
      appBar: AppBar(
        title: Text(name.toString()),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: ListView(
          children: [
            const Icon(
              Icons.shield,
              size: 100,
            ),
            const SizedBox(height: 20),
            Text(
              name.toString(),
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontSize: 30,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 30),
            buildInfo('Powerstats', hero['powerstats']),
            buildInfo('Biography', hero['biography']),
            buildInfo('Appearance', hero['appearance']),
            buildInfo('Work', hero['work']),
          ],
        ),
      ),
    );
  }

  Widget buildInfo(String title, dynamic data) {
    if (data == null) {
      return const SizedBox();
    }

    return Card(
      margin: const EdgeInsets.only(bottom: 15),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              title,
              style: const TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 10),
            Text(data is Map ? data.entries.map((e) {
              return '${e.key}: ${e.value}';
            }).join('\n') : data.toString()),
          ],
        ),
      ),
    );
  }
}