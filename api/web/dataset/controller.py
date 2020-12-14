from fastapi import APIRouter

from api import ok

router = APIRouter()

from .manager import datasetManager, OdsbibDeleteForm, OdsbibUpdateForm


@router.get('/list/names')
def list_names():
    datas = datasetManager.list_names()
    return ok(data=datas)

@router.get('/list/{dsid}')
def list(dsid):
    datas = datasetManager.list_dataset(dsid)
    return ok(data=datas)

@router.get('/delete/{dsid}')
def delete(dsid):
    datasetManager.delete(dsid)
    return ok()

from urllib import parse

@router.get('/rename/{dsid}/{newName}')
def rename(dsid, newName):
    newName = parse.unquote(newName)
    datasetManager.rename(dsid, newName)
    return ok()


@router.post('/odsbib/delete')
def odsbibdelete(form : OdsbibDeleteForm):
    datasetManager.deleteOdsbibById(form.ids)
    return ok()


@router.post('/odsbib/update')
def odsbibupdate(form : OdsbibUpdateForm):
    datasetManager.updateOdsbib(form)
    return ok()