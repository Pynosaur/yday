genrule(
    name = "yday_bin",
    srcs = glob(["app/**/*.py", "doc/**/*.yaml"]) + [".program"],
    outs = ["yday"],
    cmd = """
        _VER=$$(grep '^version:' $(location .program) | cut -d' ' -f2)
        /opt/homebrew/bin/nuitka \
            --onefile \
            --include-data-dir=doc=doc \
            --onefile-tempdir-spec=/tmp/nuitka-yday-$$_VER \
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

