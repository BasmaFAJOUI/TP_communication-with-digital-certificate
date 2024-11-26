# Projet : Communication Sécurisée avec Certificats SSL

Ce projet met en place une communication sécurisée entre un **serveur** et un **client** en utilisant des certificats SSL auto-signés. L'objectif est d'assurer une connexion chiffrée et sécurisée entre les deux parties.

---

## Table des Matières
- [Description](#description)
- [Prérequis](#prérequis)
- [Installation et Configuration](#installation-et-configuration)
- [Exécution](#exécution)


---

## Description

Ce projet est basé sur l'utilisation de certificats SSL auto-signés pour chiffrer les communications entre un serveur et un client. Les étapes incluent :
1. Génération des certificats avec OpenSSL.
2. Utilisation de keystores Java (`.jks`) pour gérer les certificats.
3. Implémentation du serveur et du client avec Python en utilisant les bibliothèques `ssl` et `socket`.

---

## Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :
- **Python** (version 3.8 ou ultérieure)
- **OpenSSL** (pour la génération des certificats)
- **Java Keytool** (inclus avec JDK pour gérer les keystores)

---

## Installation et Configuration

### Étape 1 : Cloner le projet
Clonez ce projet depuis GitHub :
```bash
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
```
### Étape 2 : Générer les certificats
après la generation de certificat format .cer et les clé format .jks je trouve que je dois les convertis en des formats compatibles pour les utiliser en python
Générer le certificat et la clé privée pour le serveur :

```bash
openssl req -newkey rsa:2048 -nodes -keyout serverKey.pem -x509 -days 365 -out serverCertificate.pem -subj "/CN=localhost"
```
Créer un keystore Java pour le serveur (optionnel) :

```bash
keytool -importkeystore -srckeystore serverKey.jks -destkeystore serverKey.p12 -deststoretype PKCS12
```
Exporter le certificat au format .pem depuis le keystore :

```bash
keytool -exportcert -alias serverkey -keystore serverKey.jks -rfc -file serverCertificate.pem
```
Générer des certificats similaires pour le client si nécessaire :

```bash
openssl req -newkey rsa:2048 -nodes -keyout clientKey.pem -x509 -days 365 -out clientCertificate.pem -subj "/CN=localhost"
```

## Exécution
1. Lancer le serveur
Exécutez le script du serveur :

```bash
python server.py
```
2. Lancer le client
Dans une autre fenêtre de terminal, exécutez le client :

```bash
python client.py
```
ici on voit une communication sécurisée entre le serveur et le client.

