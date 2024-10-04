import React, { useState } from 'react';
import VideoList from './VideoList';
import { Container, Row } from 'react-bootstrap';


const App = () => {

  const [clickFetch, setClickFetch] = useState(0);

  return (
    <Container>
      <Row className="d-flex justify-content-center mt-2 bg-dark text-light rounded">
        <h1 className="text-center">YouTube Video Fetcher
          <a href="https://github.com/surajchoubey/youtube-fetcher-fam"> GITHUB-CODE </a>
        </h1>
      </Row>
      <VideoList clickFetch={clickFetch} setClickFetch={setClickFetch} />
    </Container>
  );
};

export default App;
