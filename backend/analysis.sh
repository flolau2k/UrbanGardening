#!/bin/sh

fail_if_err () {
    eval $2
    if [ "$?" -ne 0 ]; then
        echo "FAILED " $1
        exit 1
    fi
}

fail_if_err "FORMAT"    "[ -z $(goimports -l .) ]"
fail_if_err "TEST"      "go test ./... > /dev/null"
fail_if_err "VET"       "go vet ./..."
fail_if_err "LINT"      "golint -set_exit_status \$(go list ./...)"
fail_if_err "CYCLO"     "gocyclo -over 30 ."
