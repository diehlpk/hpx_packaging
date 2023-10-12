# HPX_packing

Collection of specification files for generating packages for [HPX]

## Building

### Fedora

How to build the local rpm package and submit it to koji for building

```bash
cd Fedora
rpmbuild --define "_topdir `pwd`" -bs hpx.spec
koji build --scratch f29 SRPMS/hpx-1.2.0-0.1.rc1.src.rpm
```

How to download a task from the server

```bash
koji download-task --arch=i686 30780666
fedora-review --rpm-spec --prebuilt --name hpx
```

How to login with two factor authentication enabled

```bash
fkinit -u 
```
