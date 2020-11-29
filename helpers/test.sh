#! /bin/bash

cd go
go test ./...
cd ..

cd python
pytest
cd ..

