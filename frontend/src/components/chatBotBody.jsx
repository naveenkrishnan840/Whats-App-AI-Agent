import React, {useContext, useRef, useState, useEffect } from "react";
import {TextareaAutosize} from "@mui/material";
import "react-chat-elements/dist/main.css"
import {Formik, Form, Field} from "formik";
import {RequestService} from "./request";
import parse from 'html-react-parser';
import {MessageList} from "react-chat-elements";
import UploadFileIcon from '@mui/icons-material/UploadFile';
import PhotoCameraIcon from '@mui/icons-material/PhotoCamera';
import KeyboardVoiceIcon from '@mui/icons-material/KeyboardVoice';
import PlayArrowOutlinedIcon from '@mui/icons-material/PlayArrowOutlined';
import LogoutIcon from '@mui/icons-material/Logout';
import Stack from '@mui/material/Stack';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import Tooltip from '@mui/material/Tooltip';
import Alert from '@mui/material/Alert';
import Snackbar from "@mui/material/Snackbar";
import {useNavigate} from "react-router-dom";
import {stateContext} from "../App";


export default function ChatBotBody () {
    const {userDet} = useContext(stateContext);
    const [chatType, setChatType] = useState("");
    const [imageBytes, setImageBytes] = useState("");
    const [audioString, setAudioString] = useState("");
    const [query, setQuery] = useState("");
    const [time, setTime] = useState(0);
    const [recording, setRecording] = useState(false)
    const navigate = useNavigate();
    const mediaRecorderRef = useRef(null);
    const audioChunkRef = useRef([]);
    const fileInputRef = useRef(null);
    const timerRef = useRef(null);
    const startTimeRef = useRef(null);
    const imagUrlRef = useRef(null);
    const hasRun = useRef(false);
    const [messages, setMessages] = useState([]);
    const [enableSend, setEnableSend] = useState(false);
    const [isDisabled, setIsDisabled] = useState(false);
    const [open, setOpen] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const heightRef = useRef(null);

    useEffect(() => {
        if (hasRun.current) return
        hasRun.current = true
        const response = RequestService("get-chat-message", {});
        response.then((res)=>{
            if(res.detail){
                res.detail.map((value, index)=>{
                    if (value[4] == "audio"){
                        setMessages((prevMsg)=>
                            [...prevMsg, {
                                position: value[3] == "Bot" ? "left" :"right",
                                type: value[4],
                                title: value[3],
                                focus: true,
                                avatar: value[3] == "Bot" ? "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg": "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg",
                                className: "text-black max-h-screen font-semibold font-mono",
                                date: new Date(Date.parse(value[5])),
                                statusTitle: "Received",
                                status: "received",
                                data: {
                                    audioURL: value[1]
                                }
                            }])
                    } else if (value[4] == "text") {
                        setMessages((prevMsg)=>
                            [...prevMsg, {
                                position: value[2] == "Bot" ? "left" :"right",
                                type: value[4],
                                title: value[3],
                                text: value[2],
                                focus: true,
                                avatar: value[3] == "Bot" ? "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg": "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg",
                                className: "text-black max-h-screen font-semibold font-mono",
                                date: new Date(Date.parse(value[5])),
                                statusTitle: "Received",
                                status: "received"
                            }])
                    } else if (value[4] == "image"){
                        setMessages((prevMsg)=>
                            [...prevMsg, {
                                position: value[3] == "Bot" ? "left" :"right",
                                type: "photo",
                                title: value[3],
                                text: value[2],
                                focus: true,
                                avatar: value[2] == "Bot" ? "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg": "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg",
                                className: "text-black max-h-screen font-semibold font-mono",
                                date: new Date(Date.parse(value[5])),
                                statusTitle: "Received",
                                status: "received",
                                data: {
                                    uri: value[1],
                                    width: 500,
                                    height: 500,
                                    size: 100,
                                }
                        }])
                    }
                })
            }
        });
    }, []);

    useEffect(() => {
        heightRef.current.scrollTop = heightRef.current.scrollHeight;
    }, [messages]);

    useEffect(() => {
        if (audioString) {
            submitRequest()
        }
        if (imageBytes){
            submitRequest()
        }
    }, [audioString, imageBytes]);

    useEffect(() => {
        setOpen(true); // Show alert on component mount
    
        const timer = setTimeout(() => {
          setOpen(false); // Hide alert after 3 seconds
        }, 3000);
    
        return () => clearTimeout(timer); // Cleanup on unmount
    }, []);

    const logOut = () => {
        navigate("/login")
    }

    function blobToBase64(blob) {
        return new Promise((resolve, reject) => {
          const reader = new FileReader();
          reader.readAsDataURL(blob);
          reader.onloadend = () => resolve(reader.result);
          reader.onerror = reject;
        });
    }
      
    // const takePhoto = async () => {
    //     imageRecorder = await navigator.mediaDevices.getUserMedia({})
    // };

    const startRecording  = async () => {
        const stream = await navigator.mediaDevices.getUserMedia({audio: true})
        const recorder = new MediaRecorder(stream)
        mediaRecorderRef.current = recorder
        audioChunkRef.current = []
        recorder.ondataavailable = (event) => {
            audioChunkRef.current.push(event.data)
        }
        recorder.start()
        setRecording(true); 
        startTimeRef.current = Date.now()
        timerRef.current = setInterval(() => {
        const elapsedTime = (Date.now() - startTimeRef.current) / 1000; // Convert to seconds
        setTime(elapsedTime.toFixed(2)); // Round to 2 decimal places
        }, 100);
    };
    
    const stopRecording = () => {
        if (mediaRecorderRef.current) {
          mediaRecorderRef.current.stop();
          setRecording(false);
          setChatType("audio")
          clearInterval(timerRef.current)
        }
          setInterval(() =>{
            blobToBase64(audioChunkRef.current[0]).then((base64String) => {
                setAudioString(base64String); // Base64 audio string
              });
          }, 3000)
    };
    //   async function blobToBase64(blob) {
    //     const arrayBuffer = await blob.arrayBuffer();
    //     const bytes = new Uint8Array(arrayBuffer);
    //     let binary = "";
    //     bytes.forEach((byte) => (binary += String.fromCharCode(byte)));
    //     return `data:${blob.type};base64,${btoa(binary)}`;
    //   }
    
    const submitRequest = () => {
        setIsLoading(true)
        let userTextInput = "";
        if (!query && chatType == "audio"){
            setMessages((prevMsg)=>
                [...prevMsg, {
                    position: "right",
                    type: "audio",
                    title: "User",
                    focus: true,
                    avatar: "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg",
                    className: "text-black max-h-screen font-semibold font-mono",
                    date: new Date(),
                    statusTitle: "Received",
                    status: "received",
                    data: {
                        audioURL: URL.createObjectURL(audioChunkRef.current[0])
                    }
                }])
            userTextInput = audioString
        } else if (!query && chatType == "image") {
            setMessages((prevMsg)=>
                [...prevMsg, {
                    position: "right",
                    type: "photo",
                    title: "User",
                    focus: true,
                    avatar: "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg",
                    className: "text-black max-h-screen font-semibold font-mono",
                    date: new Date(),
                    statusTitle: "Received",
                    status: "received",
                    data: {
                        uri: URL.createObjectURL(imagUrlRef.current),
                        width: 500,
                        height: 500,
                        size: 100,
                    }
                }])
            userTextInput = imageBytes
        } else {
            setMessages((prevMsg)=>
                [...prevMsg, {
                    position: "right",
                    type: "text",
                    title: "User",
                    focus: true,
                    avatar: "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg",
                    className: "text-black max-h-screen font-semibold font-mono",
                    date: new Date(),
                    statusTitle: "Received",
                    status: "received",
                    text: query
                }])
            userTextInput = query
        }
        if (query) setQuery("")
        const response = RequestService("whatapp-request", {"chat_type": (query != "" ? "text" : chatType), "user_text_input": userTextInput});
        
        response.then((response) => {
            if(response.detail) {
                if (response.detail["workflow"] == "audio"){
                    setMessages((prevMsg)=>
                        [...prevMsg, {
                            position: "left",
                            type: response.detail["workflow"],
                            title: "Bot",
                            focus: true,
                            avatar: "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg",
                            className: "text-black max-h-screen font-semibold font-mono",
                            date: new Date(),
                            statusTitle: "Received",
                            status: "received",
                            data: {
                                audioURL: response.detail["bytes_data"]
                            }
                        }])
                } else if (response.detail["workflow"] == "text") {
                    setMessages((prevMsg)=>
                        [...prevMsg, {
                            position: "left",
                            type: response.detail["workflow"],
                            title: "Bot",
                            text: response.detail["message"],
                            focus: true,
                            avatar: "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg",
                            className: "text-black max-h-screen font-semibold font-mono",
                            date: new Date(),
                            statusTitle: "Received",
                            status: "received"
                        }])
                } else if (response.detail["workflow"] == "image"){
                    setMessages((prevMsg)=>
                        [...prevMsg, {
                                position: "left",
                                type: "photo",
                                title: "Bot",
                                text: response.detail["message"],
                                focus: true,
                                avatar: "https://t4.ftcdn.net/jpg/02/11/61/95/360_F_211619589_fnRk5LeZohVD1hWInMAQkWzAdyVlS5ox.jpg",
                                className: "text-black max-h-screen font-semibold font-mono",
                                date: new Date(),
                                statusTitle: "Received",
                                status: "received",
                                data: {
                                    uri: response.detail["bytes_data"],
                                    width: 800,
                                    height: 700,
                                    size: 300,
                                }
                            }
                        ])
                }
            }
            setIsLoading(false);
        });
    }

    const handleIconClick = () => {
        fileInputRef.current.click()
    }

    const handleFileChange = (event) => {
        const file = event.target.files[0]
        imagUrlRef.current = file;
        if(file){
            const reader = new FileReader();
            reader.onloadend = () => {
                setImageBytes(reader.result)
            }
            reader.readAsDataURL(file)
        }
        setChatType("image")
    }

    const handleSend = (event) => {
        if(event.target.value == ""){
            setEnableSend(false)
        } else {
            setEnableSend(true)
        }
        setQuery(event.target.value)
    }

    return (
        <>
            {/* <Alert onClose={()=>{setOpen(false)}} severity="success">Youtube Url is not valid. Can you check the url</Alert> */}
            <Snackbar className="w-full" anchorOrigin={{ vertical: "top", horizontal: "center" }} open={open} autoHideDuration={3000} onClose={() => setOpen(false)}>
                <Alert onClose={() => setOpen(false)} severity="success">
                    What's App Login SuccessFully
                </Alert>
            </Snackbar>
            <div className="">
                <Stack direction="row" spacing={2} className=" p-2 h-14 shadow-md rounded-md text-wrap font-mono font-extrabold text-lg text-white">
                    <Avatar alt="Avatar" src="https://t4.ftcdn.net/jpg/09/84/41/77/360_F_984417740_gYxjkB4WOCqAnZVvxLwVUPm7sEQK7hBQ.jpg" />
                    <Stack direction="column" className="mb-2">
                        <span>{userDet && userDet[1]}</span>    
                        <span>{userDet && userDet[2]}</span>
                    </Stack>   
                        <Tooltip title="Logout">
                            <IconButton onClick={logOut} sx={{color:"#25d366", height: "32px", width: "35px", left: "1000px"}} className="relative border-1 bg-white rounded-lg cursor-pointer">
                                <LogoutIcon />
                            </IconButton>
                        </Tooltip>
                </Stack>
                <div className="rounded-md overflow-y-auto text-white shadow-lg" style={{height: "480px", width: "auto", 
                backgroundImage: 'url(../static/peakpx.png)'}}>
                    <MessageList referance={heightRef} dataSource={messages}/>
                </div>
                <Formik
                    validateOnBlur={false}
                    validateOnChange={false}
                        initialValues={{ query: ""}}
                        onSubmit={async (values, { resetForm }) => {
                            submitRequest(values)
                            resetForm({
                                values: { query: ""}
                            })
                        }}
                        // validationSchema={formValidationSchema}
                    >
                        {({ setFieldValue, values, submitForm, errors }) => (
                            <Form>
                                <div className="">
                                    <Field name="query">
                                        {({ field }) => (
                                            <>
                                                <div className="flex flex-row">
                                                    <div style={{border: "2px solid #25d366"}} className="focus:cursor-pointer w-full cursor-text rounded-xl px-2.5 py-1">
                                                        <div className="max-w-full flex-1">
                                                            <div className="overflow-auto">
                                                                <TextareaAutosize disabled={isLoading} required onChangeCapture={handleSend} value={query} style={{color: "white"}} className="placeholder:text-green-500 focus:outline-none block w-full border-0 bg-transparent px-0 py-2" autoFocus="" placeholder="Message">
                                                                </TextareaAutosize>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <input
                                                        type="file"
                                                        accept="image/*"
                                                        ref={fileInputRef}
                                                        style={{ display: "none" }}
                                                        onChange={handleFileChange}
                                                    />
                                                    <Tooltip title="Upload Image">
                                                        <IconButton disabled={isLoading} onClick={handleIconClick} sx={{color:"#25d366", height: "32px", width: "35px", cursor: "pointer"}} className="relative border-1 bg-white rounded-lg  right-20 top-3 cursor-pointer">
                                                            <UploadFileIcon/> 
                                                        </IconButton>
                                                    </Tooltip>
                                                    <Tooltip title="Take photo">
                                                        <IconButton disabled={isLoading} sx={{color:"#25d366", height: "32px", width: "35px"}} className="relative border-1 bg-white rounded-lg right-20 top-3 cursor-pointer">
                                                            <PhotoCameraIcon/> 
                                                        </IconButton>
                                                    </Tooltip>
                                                    {enableSend && <Tooltip title="send">
                                                        <IconButton disabled={isLoading} onClick={submitRequest} sx={{background: "#25d366", color: "black", height: "32px", width: "35px"}} className="relative border-1 rounded-lg right-16 top-3 cursor-pointer">
                                                            <PlayArrowOutlinedIcon /> 
                                                        </IconButton>
                                                    </Tooltip>}
                                                    {!enableSend && 
                                                    <>
                                                        <Tooltip title={recording ? "Stop Recording" : "Start Recording"}>
                                                            <IconButton disabled={isLoading} onClick={recording ? stopRecording : startRecording} sx={{background: "#25d366", color: "black", height: "32px", width: "35px"}} className="relative border-1 bg-white rounded-lg right-16 top-3 cursor-pointer">
                                                                <KeyboardVoiceIcon/> 
                                                            </IconButton>
                                                        </Tooltip>
                                                        {recording && <p className="text-white">Duration: {time}</p>}
                                                    </>}
                                                </div>
                                            </>
                                        )}
                                    </Field>
                                </div>
                            </Form>
                        )}
                </Formik>
            </div>
        </>
    )
}