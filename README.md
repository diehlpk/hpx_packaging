# HPX_packing

Collection of specification files for generating packages for [HPX]

## Building

### Fedora

```bash
cd Fedora
rpmbuild --define "_topdir `pwd`" -bs hpx.spec
koji build --scratch f29 SRPMS/hpx-1.2.0-0.1.rc1.src.rpm
```

```bash
koji download-task --arch=i686 30780666
fedora-review --rpm-spec --prebuilt --name hpx
```