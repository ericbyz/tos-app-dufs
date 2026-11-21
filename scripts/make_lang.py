#!/usr/bin/env python3
"""Generate dufs.lang for the TOS App Center (26 locales, English fill)."""
NAME_EN = "dufs File Server"
AUTHOR = "ericbyz"
DESC_EN = (
    "Lightweight file server with web UI and WebDAV: browse, upload, download, "
    "edit and share files from the NAS shared folder in any browser "
    "(http://<NAS>:18242, basic auth generated at install). Single musl static "
    "binary, zero dependencies. Packaged unmodified from upstream sigoden/dufs "
    "(Apache-2.0); serve root defaults to /Volume1/public."
)
NOTE_EN = "1. Repackaged upstream sigoden/dufs (Apache-2.0) unmodified for TOS."
NOTE_ZH = "1. 将上游 sigoden/dufs(Apache-2.0)原样封装为 TOS 应用。"

PRIMARY = [
    ("zh-cn", "dufs 轻量文件服务器",
     "浏览器直接管理 NAS 共享文件夹:浏览/上传/下载/在线编辑/断点续传,支持 WebDAV 协议,"
     "手机电脑都能用。访问 http://<NAS>:18242(账号 dufs,密码安装时自动生成,存于 "
     "/etc/dufs/dufs.env)。单 musl 静态二进制零依赖,上游原样封装(Apache-2.0),"
     "共享目录默认 /Volume1/public,可在 /etc/dufs/dufs.env 修改。"),
    ("zh-hk", "dufs 輕量文件服務器",
     "瀏覽器直接管理 NAS 共享文件夾:瀏覽/上傳/下載/在線編輯/斷點續傳,支持 WebDAV 協議,"
     "手機電腦都能用。訪問 http://<NAS>:18242(賬號 dufs,密碼安裝時自動生成,存於 "
     "/etc/dufs/dufs.env)。單 musl 靜態二進制零依賴,上游原樣封裝(Apache-2.0)。"),
]

ORDER = ["zh-cn", "zh-hk", "en-us", "ko-kr", "ja-jp", "de-de", "fr-fr", "it-it",
         "es-es", "hu-hu", "pl-pl", "tr-tr", "ru-ru", "pt-pt", "cs-cz", "da-dk",
         "nl-nl", "nb-no", "sv-se", "el-gr", "ro-ro", "th-th", "vi-vn", "id-id",
         "ar-sa", "he-il"]

NATIVE = {
    "ja-jp": "ブラウザで NAS の共有フォルダを直接操作:閲覧・アップロード・ダウンロード・編集・レジューム転送、WebDAV 対応。http://<NAS>:18242(ユーザー dufs、パスワードはインストール時に生成)。単一 musl 静的バイナリで依存なし、上流を無改修でパッケージ化(Apache-2.0)。",
    "ko-kr": "브라우저에서 NAS 공유 폴더를 직접 관리: 열람·업로드·다운로드·편집·이어받기, WebDAV 지원. http://<NAS>:18242 (계정 dufs, 비밀번호는 설치 시 생성). 단일 musl 정적 바이너리, 무의존성. 업스트림 무수정 패키징(Apache-2.0).",
    "de-de": "Verwalten Sie den NAS-Ordner direkt im Browser: Ansehen, Hochladen, Herunterladen, Bearbeiten, Resume und WebDAV. http://<NAS>:18242 (Benutzer dufs, Passwort bei Installation generiert). Einziges musl-statisches Binary, keine Abhängigkeiten. Upstream unverändert (Apache-2.0).",
    "fr-fr": "Gérez le dossier partagé du NAS directement dans le navigateur : consulter, téléverser, télécharger, éditer, reprise de transfert et WebDAV. http://<NAS>:18242 (utilisateur dufs, mot de passe généré à l'installation). Binaire musl statique unique, zéro dépendance. Amont intact (Apache-2.0).",
    "es-es": "Gestione la carpeta compartida del NAS directamente en el navegador: ver, subir, descargar, editar, reanudación y WebDAV. http://<NAS>:18242 (usuario dufs, contraseña generada al instalar). Binario musl estático único, sin dependencias. Upstream intacto (Apache-2.0).",
    "ru-ru": "Управляйте общей папкой NAS прямо в браузере: просмотр, загрузка, скачивание, редактирование, докачка и WebDAV. http://<NAS>:18242 (пользователь dufs, пароль генерируется при установке). Единственный musl-статический бинарник без зависимостей. Оригинал без изменений (Apache-2.0).",
}

def main(out_path):
    lines = []
    for loc in ORDER:
        name, desc = NAME_EN, NATIVE.get(loc, DESC_EN)
        for l, n, d in PRIMARY:
            if l == loc:
                name, desc = n, d
                break
        note = NOTE_ZH if loc in ("zh-cn", "zh-hk") else NOTE_EN
        lines += [f"[{loc}]", f'name = "{name}"', f'auth = "{AUTHOR}"',
                  f'descript = "{desc}"', f'note = "{note}"', ""]
    open(out_path, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
    print("wrote", out_path, len(ORDER), "locales")

if __name__ == "__main__":
    main("dufs.lang")
