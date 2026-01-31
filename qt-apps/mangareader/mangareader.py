import info
from CraftConfig import *
from CraftOS.osutils import OsUtils

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.displayName = "MangaReader"
        self.description = "A manga reader for local files. Works with folders and archives (zip, rar, tar, 7z, cbz, cbr, cbt, cb7)."
        self.svnTargets["master"] = "https://github.com/g-fb/mangareader"
        self.defaultTarget = "2.3.0"
        
        for ver in ["2.3.0"]:
            self.targets[ver] = f"https://github.com/g-fb/mangareader/archive/refs/tags/{ver}.tar.gz"
            self.targetInstSrc[ver] = f"mangareader-{ver}"
            self.archiveNames[ver] = f"mangareader-{ver}.tar.gz"

        self.targetDigests["2.3.0"] = (["e7804ce8360a478060d8daf0b6389390f7b16140000f2efae56c1b16c6092314"], CraftHash.HashAlgorithm.SHA256)
        # self.patchToApply["2.3.0"] = [("patch.diff", 1)]

    def setDependencies( self ):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None
        self.runtimeDependencies["kde/plasma/breeze"] = None
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kconfigwidgets"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = None

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def createPackage(self):
        self.defines["executable"] = "bin\\mangareader.exe"

        # mangareader icons
        self.defines["icon"] = os.path.join(self.packageDir(), "mangareader.ico")
        self.defines["icon_png"] = os.path.join(self.sourceDir(), "mangareader", "icons", "windows", "150-apps-mangareader.png")
        self.defines["icon_png_44"] = os.path.join(self.sourceDir(), "mangareader", "icons", "windows", "44-apps-mangareader.png")


        self.defines["mimetypes"] = ["application/zip", "application/vnd.comicbook+zip", "application/x-7z-compressed", "application/x-cb7", "application/x-tar", "application/x-cbt", "application/vnd.rar", "application/vnd.comicbook-rar"]
        self.defines["file_types"] = [".zip", ".cbz", ".7z", ".cb7", ".tar", ".cbt", ".rar", ".cbr"]

        self.ignoredPackages.append("binary/mysql")

        return TypePackager.createPackage(self)
 
