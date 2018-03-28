def test_apt_sources_file(host):
    f = host.file("/etc/apt/sources.list")
    assert f.exists
    assert f.is_file
