$path = read-host "Geef hier het pad op wat je wilt uitvragen"
$size = Read-Host "Geef hier de grootte op in MB"
$size = [int64]$Size * 1MB
$Files = Get-ChildItem -Path $path -Recurse | Where-Object -FilterScript {($_.Length -ge $size)} | Sort-Object -Descending length | select -First 10
ForEach ($File in $Files){

    $FileName = $File.FullName

    $FileSize = ("{0:N2} mB" -f((Get-Item $file.FullName).length/1MB))

    Write-Host $FileName " : " $FileSize

}