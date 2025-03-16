import {React, useContext} from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { TextField, Button, Container, Box, Typography } from '@mui/material';
import {RequestService} from "./request"
import { useNavigate } from 'react-router-dom';
import {stateContext} from "../App";

// Validation Schema using Yup
const validationSchema = Yup.object({
  name: Yup.string().required('Name is required'),
  phone: Yup.string()
    .matches(
      /^[0-9]{10}$/,
      'Phone number must be 10 digits'
    )
    .required('Phone number is required'),
});

const LoginPage = () => {
  const navigate = useNavigate();
  const {setUserDet} = useContext(stateContext);
  // Formik setup
  const formik = useFormik({
    initialValues: {
      name: '',
      phone: '',
    },
    validationSchema,
    onSubmit: async (values) => {
      // const response = await fetch('http://127.0.0.1:8006/signup-login', {
      //     method: 'POST',
      //     headers: {
      //         'Content-Type': 'application/json',
      //     },
      //     body: JSON.stringify({"name": values.name, "phone_no": values.phone}) ,
      // });
      const response = RequestService("signup-login", {"name": values.name, "phone_no": values.phone});

      response.then((response) => {
        if(response.detail["status"] == "login success") {
          setUserDet(response.detail["user"])
          navigate("/whatappAI")
          
        }
      });
      console.log('Form Data', values);
    },
  });

  return (
    <Container maxWidth="xs" className="bg-white p-8 rounded-lg shadow-md" sx={{position: "relative", top: "120px", backgroundImage: 'url(../static/peakpx.png)'}}>
      <Box>
        <Typography variant="h5" align="center" gutterBottom className='text-white'>
          Signup/Login
        </Typography>
        <form onSubmit={formik.handleSubmit} className="space-y-4">
          {/* Name Input */}
          <TextField
             sx={{ input: { color: 'white'}}} 
            label="Name"
            variant="outlined"
            fullWidth
            name="name"
            value={formik.values.name}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            error={formik.touched.name && Boolean(formik.errors.name)}
            helperText={formik.touched.name && formik.errors.name}
            required
          />

          {/* Phone Number Input */}
          <TextField
            label="Phone Number"
            variant="outlined"
            sx={{ input: { color: 'white'}}}
            fullWidth
            name="phone"
            value={formik.values.phone}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            error={formik.touched.phone && Boolean(formik.errors.phone)}
            helperText={formik.touched.phone && formik.errors.phone}
            required
            inputProps={{
              maxLength: 10,
            }}
          />

          {/* Submit Button */}
          <Button
            type="submit"
            variant="contained"
            color="primary"
            fullWidth
            className="mt-4"
          >
            Login
          </Button>
        </form>
      </Box>
    </Container>
  );
};

export default LoginPage;
