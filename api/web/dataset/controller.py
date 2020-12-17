from fastapi import APIRouter
from threading import Thread
from urllib import parse

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

@router.get('/clean/{dsid}')
def clean(dsid):
    userid = 'test'
    CleanDatasetThread(dsid, userid).start()
    return ok()

class CleanDatasetThread(Thread):
    def __init__(self, dsid = '', userid = ''):
        super().__init__()
        self.dsid = dsid
        self.userid = userid

    def run(self) -> None:
        if self.dsid:
            datasetManager.clean(self.dsid, self.userid)

@router.get('/show/process/{dsid}')
def show_process(dsid):
    dim_ds = datasetManager.showProcess(dsid)
    return ok(data=dim_ds)

@router.get('/delete/{dsid}')
def delete(dsid):
    datasetManager.delete(dsid)
    return ok()


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