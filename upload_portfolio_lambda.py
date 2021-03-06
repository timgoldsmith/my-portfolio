import boto3
import StringIO
import zipfile
import mimetypes


def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    build_bucket = s3.Bucket('build.porfolio.mathisonit.co.uk')
    portfolio_bucket = s3.Bucket('portfolio.mathisonit.co.uk')

    build_bucket.download_file('Portfoliobuild.zip', 'C:\\temp\\Portfoliobuild.zip')

    with zipfile.ZipFile('C:\\temp\\Portfoliobuild.zip') as myzip:
        for nm in myzip.namelist():
            #print nm
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
            portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

    print "Hello from lambda"
