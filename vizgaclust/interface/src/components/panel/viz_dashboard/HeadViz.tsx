import * as React from 'react';
import { Header,Heading, Box } from 'grommet';

function HeadViz(){
    return(
        <Header background="#2a3142">
            <Box pad="small">
                <Heading margin="none" level={4}> Visualize Selection </Heading>
            </Box>
        </Header>
    )
}

export default HeadViz;