# Android Mobile App & Cloud APK Pipeline
### Modern Android SDK 34 Architecture + Automated Free Cloud CI/CD

A production-ready Android template configured for modern SDK 34 standards, featuring a native Android wrapper, offline caching, responsive UI, and automated cloud APK builds via GitHub Actions.

---

## Features
- **Modern SDK**: `compileSdk 34`, `minSdk 24`, `targetSdk 34`.
- **Native Android Wrapper**: High-performance `MainActivity.java` with hardware acceleration, responsive viewport scaling, and DOM storage.
- **Zero Local SDK Requirement**: Automatically builds release APKs (`app-release.apk`) directly in GitHub Actions using free `ubuntu-latest` cloud runners.
- **Ready for Release**: Signing configs and automated artifact uploads included.

---

## Compiling the APK

### Option 1: Free Cloud Build (GitHub Actions - Recommended)
1. Push this repository to GitHub.
2. Navigate to **Actions** > **Build Signed Android Release APK**.
3. Click **Run workflow**. In 3 minutes, your compiled `.apk` will be available in the **Artifacts** download section!

### Option 2: Local Build (Android Studio / Gradle)
```bash
./gradlew assembleRelease
```
The output `.apk` will be generated at `app/build/outputs/apk/release/app-release.apk`.
