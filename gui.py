import PySimpleGUI as sg
import zip_converters as zc

compress_label = sg.Text("Select files to compress")
compress_input = sg.Input()
compress_choose_button1 = sg.FilesBrowse("Choose", key="files")

compress_dest_label = sg.Text("Select Destination folder: ")
compress_input_dest = sg.Input()
cpress_chse_fld_button = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text("", key="output compression", text_color='black')

extractor_title = sg.Text("Select a Zip to extract")

archive_label = sg.Text("Select Archive:")
archive_input = sg.Input()
extract_choose_button1 = sg.FileBrowse("Choose", key="extract archive")

extract_dest_dir = sg.Text("Select dest dir:")
extract_input_dest_dir = sg.Input()
extract_choose_button2 = sg.FolderBrowse("Choose", key="extract folder")

extract_button = sg.Button("Extract")
extract_status = sg.Text(key="output extract", text_color='black')

exit_button = sg.Button("Exit")

window = sg.Window("Zip Compressor/Extractor",
                   layout=[[compress_label, compress_input, compress_choose_button1],
                           [compress_dest_label, compress_input_dest, cpress_chse_fld_button],
                           [compress_button, output_label],
                           [extractor_title],
                           [archive_label, archive_input,
                            extract_choose_button1],
                           [extract_dest_dir, extract_input_dest_dir,
                            extract_choose_button2],
                           [extract_button, extract_status],
                           [exit_button]
                           ])

while True:
    event, values = window.read()
    match event:
        case "Compress":
            filepaths = values["files"].split(";")
            folder = values["folder"]
            zc.make_archive(filepaths, folder)
            window["output compression"].update(value="Compression completed!")
        case "Extract":
            archivepath = values["extract archive"]
            dest_dir = values["extract folder"]
            zc.extract_archive(archivepath, dest_dir)
            window["output extract"].update(value="Extraction Completed")
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
