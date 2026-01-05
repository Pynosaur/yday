genrule(
    name = "yday_bin",
    srcs = glob(["app/**/*.py", "doc/**/*.yaml"]),
    outs = ["yday"],
    cmd = """
        /opt/homebrew/bin/nuitka \
            --onefile \
            --include-data-dir=doc=doc \
            --onefile-tempdir-spec=/tmp/nuitka-yday \
            --no-progressbar \
            --assume-yes-for-downloads \
            --no-deployment-flag=self-execution \
            --output-dir=$$(dirname $(location yday)) \
            --output-filename=yday \
            $(location app/main.py)
    """,
    local = 1,
    visibility = ["//visibility:public"],
)

