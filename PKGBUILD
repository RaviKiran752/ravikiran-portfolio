# Maintainer: Ravi Kiran <ravi742t7p@gmail.com>
pkgname=ravikiran-portfolio
pkgver=1.0.0
pkgrel=1
pkgdesc="Terminal-based interactive portfolio of Ravi Kiran"
arch=('any')
url="https://github.com/RaviKiran752/ravikiran-portfolio"
license=('MIT')
depends=('python' 'python-rich')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -Dm755 portfolio.py "$pkgdir/usr/bin/ravikiran"
}
