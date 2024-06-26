import 'package:flutter/material.dart';
import 'package:nour_app/generated/l10n.dart';
import 'package:nour_app/screens/signUp_screen.dart';
import 'package:nour_app/widgets/localization_icon.dart';
import 'package:nour_app/screens/hopeful_and_calm.dart';
import 'package:nour_app/screens/login_screen.dart';

class Welcome extends StatefulWidget {
  const Welcome({Key? key}) : super(key: key);

  @override
  State<Welcome> createState() => _WelcomeState();
}

class _WelcomeState extends State<Welcome> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const LocalizationIcon(),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [
              Theme.of(context).colorScheme.primary,
              Theme.of(context).colorScheme.secondary,
            ],
            begin: Alignment.bottomLeft,
            end: Alignment.topRight,
          ),
        ),
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Center(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text(
                      S.of(context).welcome,
                      style: const TextStyle(
                        fontSize: 30,
                        color: Colors.black,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 20),
                    ElevatedButton(
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => const LoginScreen()),
                        );
                      },
                      style: ElevatedButton.styleFrom(
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(20)),
                        fixedSize: const Size(200, 55),
                        backgroundColor: Theme.of(context).colorScheme.surface,
                      ),
                      child: Text(
                        S.of(context).sign_in,
                        style: const TextStyle(
                          fontSize: 20,
                          color: Color.fromARGB(255, 255, 251, 251),
                        ),
                      ),
                    ),
                    const SizedBox(height: 10),
                    ElevatedButton(
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => const NewAccount()),
                        );
                      },
                      style: ElevatedButton.styleFrom(
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(20)),
                        fixedSize: const Size(200, 55),
                        backgroundColor: Theme.of(context).colorScheme.surface,
                      ),
                      child: Text(
                        S.of(context).new_account,
                        style: const TextStyle(
                          fontSize: 20,
                          color: Color.fromARGB(255, 255, 251, 251),
                        ),
                      ),
                    ),
                    const SizedBox(height: 50),
                    ElevatedButton(
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => const HopefulAndCalm()),
                        );
                      },
                      style: ElevatedButton.styleFrom(
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(20)),
                        fixedSize: const Size(128, 55),
                        backgroundColor: Theme.of(context).colorScheme.surface,
                      ),
                      child: Text(
                        S.of(context).skip,
                        style: const TextStyle(
                          fontSize: 20,
                          color: Color.fromARGB(255, 255, 251, 251),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
